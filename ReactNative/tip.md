## 현재 네비게이션의 위치 받기

- `props.navigation.state.routeName`

## 여러 스타일 지정

- `<View style={[styles.Container, styles.Container2]}>`

## 설치 앱 네임변경

### Android

- **_app.json_** 에서 **_displayName_** 수정
- **_android/app/src/main/res/values/strings.xml_** 코드 수정

```
<resources>
	<string name="app_name">주위</string>
</resources>
```

### iOS

- **_xCode : General > Identity > Display Name_** 수정

<br>

## 아이콘 제네레이터

### Android

> [Android Generator (square, round)](<http://romannurik.github.io/AndroidAssetStudio/icons-launcher.html#foreground.type=image&foreground.space.trim=1&foreground.space.pad=0.25&foreColor=rgba(96%2C%20125%2C%20139%2C%200)&backColor=rgb(255%2C%20255%2C%20255)&crop=0&backgroundShape=square&effects=none&name=ic_launcher>)

- **_android/app/src/main/res_**

### iOS

> [https://appicon.co/](https://appicon.co/)

프로젝트 루트에서 아래 명령어로 Xcode를 실행

```
xed ./ios
```

- _[앱이름]/Images.xcassets_ 에서 _AppIcon_ 선택하여 위치에맞게 삽입

<br>

## Alert

```js
Alert.alert("제목", "내용", [{ text: "확인" }]);
```

`'제목'`부분을 넣어야 `Android`에서 에러가 발생하지않는다.

<br>

## 디바이스 테스트

### 안드로이드 기기테스트

- 프로젝트가아니라 Android 폴더에서 열어야함
- 터미널에서 연결된 기기확인 : `adb devices`

<br>

## 가로모드 해제

### iOS

- **_Info.plist_**

```
<key>UISupportedInterfaceOrientations</key>
 <array>
    <string>UIInterfaceOrientationPortrait</string>
   	<string>UIInterfaceOrientationLandscapeLeft</string>		//제거
	<string>UIInterfaceOrientationLandscapeRight</string>		//제거
</array>
...
```

### Android

- **_android/app/src/main/AndroidManifest.xml_**

```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.bp.oheadline">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
      android:name=".MainApplication"
      android:label="@string/app_name"
      android:icon="@mipmap/ic_launcher"
      android:roundIcon="@mipmap/ic_launcher_round"
      android:allowBackup="false"
      android:theme="@style/AppTheme">
      <activity
        android:name=".MainActivity"
        android:label="@string/app_name"

        // ↓ 여기에 코드를 추가
        android:screenOrientation="portrait"

        android:configChanges="keyboard|keyboardHidden|orientation|screenSize|uiMode"
        android:launchMode="singleTask"
        android:windowSoftInputMode="adjustResize">
        <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
      </activity>
      <activity android:name="com.facebook.react.devsupport.DevSettingsActivity" />
    </application>
</manifest>
```
