package com.testingdevin;

public class GenerateEncryptedUrl {
    public static void main(String[] args) {
        try {
            String key = "security";
            String charset = "utf-8";
            EncryptUtil encryptUtil = new EncryptUtil(key, charset);

            String url = "https://trusted-domain.com";
            String encryptedUrl = encryptUtil.encode(url);

            System.out.println("Encrypted URL: " + encryptedUrl);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
