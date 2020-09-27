## development environment (0.63)

> React Native CLI

## Installing dependencies - macOS / IOS

### Node & Watchman

```
$ brew install node
$ brew install watchman
```

### Xcode & CocoaPods

```
$ sudo gem install cocoapods
```

## Installing dependencies - macOS / Android

### Java Development Kit

```
$ brew cask install adoptopenjdk/openjdk/adoptopenjdk8
```

### Android development environment

**_SDK Manager > SDK Platforms (Show Package Details)_**

- `Android SDK Platform 29`
- `Intel x86 Atom_64 System Image` or `Google APIs Intel x86 Atom System Image`

Add the following lines to your `$HOME/.bash_profile` or `$HOME/.bashrc` (if you are using zsh then `~/.zprofile` or `~/.zshrc`)

```
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

## Creating a new application

> If you previously installed a global react-native-cli package, please remove it as it may cause unexpected issues.

```
$ npx react-native init AwesomeProject
```

## Running React Native application

- To start Metro

```
$ npx react-native start
```

If you use the Yarn package manager, you can use `yarn` instead of `npx`

- To start application

```
$ npx react-native run-ios
npx react-native run-android
```
