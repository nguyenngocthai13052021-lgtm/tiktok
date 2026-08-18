[app]

title = TikTok Ghost
package.name = tiktokghost
package.domain = org.test

source.main = toole.py
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,requests
orientation = portrait

# Bắt buộc phải có dòng này để GitHub tự động đồng ý điều khoản Android SDK
android.accept_sdk_license = True
