package com.testingdevin;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.logging.Logger;

public class EncryptUtil {

    private final String key;
    private final String charset;
    private static final Logger logger = Logger.getLogger(EncryptUtil.class.getName());

    public EncryptUtil(String key, String charset) {
        // Ensure the key length is 16 bytes for AES
        if (key.length() < 16) {
            this.key = String.format("%-16s", key).substring(0, 16);
        } else {
            this.key = key.substring(0, 16);
        }
        this.charset = charset;
    }

    public String encode(String data) throws Exception {
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(charset), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] encryptedData = cipher.doFinal(data.getBytes(charset));
        return Base64.getEncoder().encodeToString(encryptedData);
    }

    public String decode(String encryptedData) throws Exception {
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(charset), "AES");
        Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5PADDING");
        cipher.init(Cipher.DECRYPT_MODE, secretKey);
        byte[] decodedData = Base64.getDecoder().decode(encryptedData);

        logger.info("Decoded data length: " + decodedData.length);
        logger.info("Decoded data (Base64): " + Base64.getEncoder().encodeToString(decodedData));

        // Ensure the input length is a multiple of 16 by adding padding if necessary
        int paddingLength = 16 - (decodedData.length % 16);
        byte[] paddedData = new byte[decodedData.length + paddingLength];
        System.arraycopy(decodedData, 0, paddedData, 0, decodedData.length);

        byte[] decryptedData;
        try {
            decryptedData = cipher.doFinal(paddedData);
        } catch (Exception e) {
            logger.severe("Decryption error: " + e.getMessage());
            logger.severe("Decoded data length: " + decodedData.length);
            logger.severe("Decoded data (Base64): " + Base64.getEncoder().encodeToString(decodedData));
            throw e;
        }

        // Remove padding after decryption
        int unpaddedLength = decryptedData.length - paddingLength;
        byte[] unpaddedData = new byte[unpaddedLength];
        System.arraycopy(decryptedData, 0, unpaddedData, 0, unpaddedLength);

        String result = new String(unpaddedData, charset);
        logger.info("Decryption successful, result: " + result);
        return result;
    }
}
