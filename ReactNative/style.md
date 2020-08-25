## Start

### Expo

```
$ npm install --global expo-cli

$ expo init my-project
```

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

`marginVertical` = `marginBotton` + `marginTop`과 같다.

### shadow

- `shadowColor`, `shadowOffset` 같은 shadow 속성은 IOS애서만 가능
- Android는 `elevation`으로 가능
