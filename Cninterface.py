import requests
login="https://browser-test.antuzhi.com/maccount/account/user_login"

loginpara="/?user_id=zh506&time=1565936608105&sign=5969f6cd8c59146eaac84f464de9fb47&token=zh506.1010012.b60bd68a266649b5cbcfed15aec95d73.1565936608924&channel_id=0&timestamp=1565936608123&code=CN&language=zh&versionCode=7&versionName=1.0.6.105"
p=login+loginpara
print(requests.post(p).text)