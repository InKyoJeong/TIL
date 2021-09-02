## WARNING: UNPROTECTED PRIVATE KEY FILE!

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'YOUR_KEY.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "YOUR_KEY.pem": bad permissions
```

- 퍼미션이 공개되어있어서 생기는 문제
- private key의 퍼미션을 변경하면 된다.

```bash
$ chmod 400 your_key.pem
```

- `chmod` : 파일의 접근 권한을 변경하는 명령 (change mod)
- `400` : 읽기만 가능
- `600` : 읽기와 쓰기 가능
