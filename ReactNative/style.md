## Style

### inline style

```js
<View
    style={{
        flexDirection: "row",
        justifyContent: "space-between",
        alignItems: "center",
    }}
>
```

### StyleSheet Objects

```js
<View style={styles.tomato}>
  <View style={styles.inputContainer}>...</View>
</View>;

const styles = StyleSheet.create({
  tomato: {
    padding: 50,
  },
  inputContainer: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
});
```

### marginVertical

`marginVertical` = `marginBotton` + `marginTop`

### shadow

- `shadowColor`, `shadowOffset` 같은 shadow 속성은 IOS에서만 가능
- Android는 `elevation`으로 가능

### <ScrollView>

- `<ScrollView>` 태그에서는 `style`대신 `contentContainerStyle`사용

```js
<ScrollView contentContainerStyle={styles.list}>
```

### ScrollView & FlatList

- `FlatList` : optimized for **very long lists** or lists where you don't **know how long**
- `ScrollView`: great for scrollable content which **isn't infinitely long**

<br>

## <View> vs <Text>

- `<Text>`태그 안의 `<Text>`태그는 리액트네이티브에서 **예외적으로** 바깥에서 정의된 스타일도 받는다.
- `<View>`는 Flexbox를 사용하지만, `<Text>`는 사용하지 않음

<br>

## Icon

- expo : [https://icons.expo.fyi/](https://icons.expo.fyi/)

### Use

> example: Ionicons

```js
import { Ionicons } from "@expo/vector-icons";

//...

<Ionicons name="md-remove" size={24} />;
```

<br>

## Device Rotate (orientations)

- expo에서 기기를 돌려보면 가로모드가 적용되지않음
- expo에서 기본값으로 락되어있음

```js
//app.json
  "expo": {
    //...
    "orientation": "portrait",    //세로모드
    //...
```

- `"orientation": "landscape",` : 가로모드 ex)게임
- `"orientation": "default",` : 회전 가능함

<br>

### KeyboardAvoidingView

- 키보드가 입력칸을 가릴경우 조절하기
- `behavior` : IOS의 경우 `position`, Android는 `padding`이 좋다.

```js
//ex)
<ScrollView>
      <KeyboardAvoidingView behavior="position" keyboardVerticalOffset={30}>
//...
```

<br>

## Dimensions.get

`Dimensions.get('window')`로 기기별 대응을 할 수 있다.

```js
//ex
width: Dimensions.get("window").width / 4,
```

- 중요한 것은, **앱이 시작될때만 계산**된다 => 가로로 전환하거나 가로에서 실행후 세로로 전환하면 깨진다.
  - `useState`, `useEffect`, `addEventListener` 등으로 조정해야함

<br>

## Font

### Fetch

- **Add Fonts** file (to asset Folder)
- `expo install expo-font`
- **_import_** `Font`, `{ AppLoading }`
- **Fecth**

```js
//...
import * as Font from "expo-font";
import { AppLoading } from "expo";

const fetchFont = () => {
  Font.loadAsync({
    "open-sans": require("./assets/fonts/OpenSans-Regular.ttf"),
    "open-sans-bold": require("./assets/fonts/OpenSans-Bold.ttf"),
  });
};

export default function App() {
  const [fontLoaded, setFontLoaded] = useState(false);

  if (!fontLoaded) {
    return (
      <AppLoading startAsync={fetchFont} onFinish={() => setFontLoaded(true)} />
    );
  }
//...
```

### Use

```js
title:{
    fontFamily: "open-sans-bold",
}
```
