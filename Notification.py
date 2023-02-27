import http.client, urllib

class Notification:
    # create connection
    conn = http.client.HTTPSConnection("api.pushover.net:443")

    # function that makes POST request, to send notification
    def send(self, customMsg):
        self.conn.request("POST", "/1/messages.json",
                          urllib.parse.urlencode({
                              "token": "aowxjw55pyox6sxmzn38hkh9eka6j7",
                              "user": "u9xqhd4hp4bvti4cfvyvjwd891n4vt",
                              "message": customMsg,
                          }), {"Content-type": "application/x-www-form-urlencoded"})
        self.conn.getresponse()
