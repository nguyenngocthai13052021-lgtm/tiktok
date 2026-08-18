[app]

title = TikTok Ghost
package.name = tiktokghost
package.domain = org.test

source.main = toole.py
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,requests
orientation = portrait

# Cấu hình Android bắt buộc
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
