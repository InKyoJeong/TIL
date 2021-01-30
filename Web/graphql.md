## GraphQL 이란?

- `GraphQL`은 클라이언트에서 서버의 데이터를 효율적으로 가져오기 위한 목적
- `SQL`은 백엔드에서 데이터베이스의 데이터를 효율적으로 가져오기 위한 목적

<br>

## GraphQL 로 해결할 수 있는 문제 2가지

### Over-fetching

- 모든 유저의 name을 웹사이트에 보여주고 싶다고 하자. GET을 사용

```
/users/ GET
```

- 그러나 users에서 사용자명만 주는게 아니라 성이나 프로필사진 등과 같은 모든 유저 정보도 준다.
- DataBase에 사용하지 않을 영역을 요청하는 방식 = 비효율적
- 이것이 over-fetching : 요청한 영역의 정보 보다, 많은 정보를 서버에서 받음

<br>

### Under-fetching

- 예를 들어, 인스타앱을 실행하면 많은 정보를 받게됨

```
/feed/
/notification/
/user/1/
```

- 인스타 피드도 받고, 알림, 유저프로필 등을 받음
- 앱을 실행하려면 이 3가지 요청을 해야함. 즉, 3가지 요청이 3번오고가야 앱이 실행됨
- 이것이 under-fetching : REST에서 하나를 완성하려고 많은 소스를 요청함

<br>

## 위의 문제를 어떻게 해결할까

- GraphQL에선 이 모든것들을 하나의 query로 할 수 있음
- query는 DB에 무언가 요청하고 graphql언어로 원하는 정보를 알려줄 수 있음

- 예를 들어, 피드의 모든 사진 피드 중 댓글이랑 좋아요 수, 알림과 알림을 확인했는지에 대한 정보, 유저의 프로필 중 사용자 명과 사진을 원한다고 하자.

```
{
    feed {
        comment
        likeNumber
    }
    notifications {
        isRead
    }
    user {
        username
        profilePic
    }
}
```

- 이게 query이다. graphql의 백엔드에 보내면 이와 같은 요청 정보를 담은 Object를 보낼것임

```
{
    feed: [
        {
            comments: 1,
            likeNumber: 20,
        }
    ],
    notifications: [
        {
            isRead: true,
        },
        {
            isRead: false,
        }
    ],
    user: {
        username: "kyo",
        profilePic: "http..."
    }
}
```

- 이게 graphql에서 보낸 javascript object이다. 요청한 것만 정확히 보내준다.
