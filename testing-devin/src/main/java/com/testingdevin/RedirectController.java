package com.testingdevin;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.net.URLEncoder;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.regex.Pattern;
import java.util.logging.Logger;

@Controller
public class RedirectController {

    private static final String ENCRYPTION_KEY = "security";
    private static final Pattern URL_PATTERN = Pattern.compile("^(https?|ftp)://[\\w.-]+(:\\d+)?(/\\S*)?$");
    private static final Logger logger = Logger.getLogger(RedirectController.class.getName());

    @GetMapping("/OpenRedirect")
    public String redirectPage(ModelMap model, @RequestParam String url, @RequestParam String storeName) {
        try {
            // Validate and encode storeName
            if (storeName == null || storeName.isEmpty() || storeName.contains("<") || storeName.contains(">")) {
                throw new IllegalArgumentException("Invalid storeName");
            }
            storeName = URLEncoder.encode(storeName, StandardCharsets.UTF_8.toString());

            // Log the URL parameter before decoding
            logger.info("Received URL parameter: " + url);

            // Remove any spaces from the URL parameter
            url = url.replace(" ", "");

            // URL decode the encrypted URL parameter
            url = URLDecoder.decode(url, StandardCharsets.UTF_8.toString());

            // Log the length of the URL-decoded encrypted data
            logger.info("Length of URL-decoded encrypted data: " + url.length());

            // Decrypt and validate URL
            EncryptUtil des = new EncryptUtil(ENCRYPTION_KEY, StandardCharsets.UTF_8.toString());
            url = des.decode(url);

            if (!URL_PATTERN.matcher(url).matches()) {
                throw new IllegalArgumentException("Invalid URL");
            }

            // Ensure the URL domain is one that we expect to redirect to
            if (!url.startsWith("https://trusted-domain.com")) {
                throw new IllegalArgumentException("Untrusted URL domain");
            }
        } catch (Exception e) {
            logger.severe("Error processing redirect: " + e.getMessage());
            url = "error";
        }

        model.addAttribute("url", url);
        model.addAttribute("storeName", storeName);
        return "redirect";
    }
}
