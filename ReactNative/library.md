## React Native Geolocation

```
$ npm install react-native-geolocation-service
```

### iOS

```
$ cd ios
$ pod install
```

- Swift 지원설정
  - **_ios/[proejct name].xcworkspace_** 실행 > 프로젝트 폴더 우클릭 > _New File..._ > _Swift File_ > _Create_ > _Create Bridging Header_ 클릭
- iOS 권한 설정
  - **_ios/[Project Name]/info.plist_**

```
<key>NSLocationWhenInUseUsageDescription</key>    //앱이 실행시만 위치 정보를 습득
<string>(권한 안내 text)</string>
```

> 만약 앱이 백그라운드에서도 위치 정보를 습득하려면 추가설정 필요

### Android

- **_android/app/src/main/AndroidManifest.xml_**

```
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```
