#include <WiFiManager.h> // https://github.com/tzapu/WiFiManager
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <stdlib.h>

#define TRIGGER_PIN 0

int timeout = 120;
String server_ip;

void setup() {
  WiFi.mode(WIFI_STA);
  Serial.begin(115200);
  Serial.println("\n Starting");
  pinMode(TRIGGER_PIN, INPUT_PULLUP);
  randomSeed(analogRead(0));
  WiFiConnect();
}

void WiFiConnect() {
  if ( digitalRead(TRIGGER_PIN) == LOW) {
    WiFiManager wm;    

    WiFiManagerParameter custom_ip("server_ip", "Server IP with port", "", 40);
    wm.addParameter(&custom_ip);

    wm.resetSettings();

    wm.setConfigPortalTimeout(timeout);

    if (!wm.startConfigPortal("HygroMonitor")) {
      Serial.println("failed to connect and hit timeout");
      delay(3000);
      ESP.restart();
      delay(5000);
    }
    server_ip = custom_ip.getValue();
    Serial.println("FlowerPot connected to WiFi :)");
  }
}

void loop() {
  test_api();
  delay(5000);
}

void test_api() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin("http://"+server_ip+"/api/get_readings/");
    http.addHeader("Content-Type", "application/json");

    StaticJsonDocument<200> jsonDoc;
    jsonDoc["humidity"] = random(0, 100);

    String jsonString;
    serializeJson(jsonDoc, jsonString);

    int httpResponseCode = http.POST(jsonString);

    if (httpResponseCode > 0) {
      Serial.print("Server response: ");
      Serial.println(httpResponseCode);
      String response = http.getString();
      Serial.println(response);
    } else {
      Serial.print("Error while sending: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.println("No WiFi connection");
  }
}


