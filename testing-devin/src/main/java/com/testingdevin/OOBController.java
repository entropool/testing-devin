package com.testingdevin;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;
import java.util.logging.Logger;

@RestController
public class OOBController {

    private static final Logger logger = Logger.getLogger(OOBController.class.getName());

    @RequestMapping(value = "/oob/{uniqueId}", method = {RequestMethod.GET, RequestMethod.POST})
    public String handleOOBRequest(@PathVariable String uniqueId, @RequestHeader Map<String, String> headers, @RequestBody(required = false) String body) {
        logger.info("Received OOB request with uniqueId: " + uniqueId);
        logger.info("Headers: " + headers.toString());
        if (body != null) {
            logger.info("Body: " + body);
        }
        return "Request received";
    }
}
