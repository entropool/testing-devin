package com.testingdevin;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class EncryptUtil {

    private final String key;
    private final String charset;

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
        byte[] decryptedData = cipher.doFinal(decodedData);
        return new String(decryptedData, charset);
    }
}
