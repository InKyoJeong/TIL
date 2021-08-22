## Protected Property and Method

- class밖에서 접근 불가
- Encapsulation과 data privacy가 필요한 이유
  - prevent code from outside of a class to accidentally manipulate
- truly private 아니고 convention임

```js
class Account {
  // Public fields
  locale = navigator.language;

  // Private fields
  #movements = [];
  #pin;

  constructor(owner, currency, pin) {
    this.owner = owner;
    this.currency = currency;
    // Protected property
    this.#pin = pin;
    // this._movements = [];
  }

  getMovements() {
    return this.#movements;
  }

  deposit(val) {
    this.#movements.push(val);
  }

  _approveLoan(val) {
    return true;
  }
}

const acc1 = new Account("Mary", "KR", 2000);
console.log(acc1.getMovements());

console.log(acc1.#movements); // Uncaught SyntaxError: Private field '#movements' must be declared in an enclosing class
console.log(acc1.#pin); //Uncaught SyntaxError: Private field '#pin' must be declared in an enclosing class

console.log(acc1); // Account {locale: "ko", owner: "Mary", currency: "KR", #movements: Array(0), #pin: 2000}
```
