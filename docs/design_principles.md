# Low-Level Design Wiki: Software Design Principles (DRY, KISS, YAGNI)

Writing maintainable and readable code requires more than just applying design patterns. You must also adhere to fundamental software engineering principles. This guide covers **DRY**, **KISS**, and **YAGNI** in Python with clear, practical examples.

---

## 1. DRY (Don't Repeat Yourself)

> **Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.**

### Real-World Analogy
Imagine a restaurant menu that lists the price of a side salad in five different places (appetizers, sides, lunch specials, kids menu, combo deals). If the price of lettuce increases, the owner must update all five sections. If they forget one, the menu becomes inconsistent. Instead, they should define the price in one place and reference it.

### Before (Bad) - Duplicate Validation Logic
Here, validation of user input is copy-pasted across different class methods. If the validation rules change, multiple locations must be updated.

```python
class RegistrationService:
    def register_user(self, email: str, username: str) -> None:
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        if len(username) < 3:
            raise ValueError("Username too short.")
        print(f"User {username} registered.")

class ProfileService:
    def update_profile(self, email: str, username: str) -> None:
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        if len(username) < 3:
            raise ValueError("Username too short.")
        print(f"Profile updated for {username}.")
```

### After (Good) - Centralized Validation Logic
Extract the validation into a dedicated, reusable function or validator class.

```python
class InputValidator:
    @staticmethod
    def validate_user_input(email: str, username: str) -> None:
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        if len(username) < 3:
            raise ValueError("Username too short.")

class RegistrationService:
    def register_user(self, email: str, username: str) -> None:
        InputValidator.validate_user_input(email, username)
        print(f"User {username} registered.")

class ProfileService:
    def update_profile(self, email: str, username: str) -> None:
        InputValidator.validate_user_input(email, username)
        print(f"Profile updated for {username}.")
```

---

## 2. KISS (Keep It Simple, Stupid)

> **Systems work best if they are kept simple rather than made complicated; simplicity should be a key goal in design.**

### Real-World Analogy
Using a hammer to hang a picture frame is simple and effective. Constructing an automated, laser-guided picture-hanging robot is over-engineered, expensive, and prone to calibration failure.

### Before (Bad) - Over-Engineered Search Function
This implementation uses complex nested structures, custom lookup wrappers, and excessive lambda functions to search for a string in a list.

```python
from typing import List, Callable, Any

class SearchCriteria:
    def __init__(self, target: str):
        self.target = target

class ListSearcher:
    def search(self, items: List[str], criteria: SearchCriteria) -> List[str]:
        wrapper: Callable[[str], bool] = lambda item: item.lower() == criteria.target.lower()
        results: List[Any] = []
        for index in range(len(items)):
            current_item = items[index]
            if wrapper(current_item):
                results.append(current_item)
        return results
```

### After (Good) - Simple, Pythonic Search
Keep it simple, readable, and utilize Python's built-in capabilities.

```python
from typing import List

class SimpleSearcher:
    def search(self, items: List[str], target: str) -> List[str]:
        target_lower = target.lower()
        return [item for item in items if item.lower() == target_lower]
```

---

## 3. YAGNI (You Aren't Gonna Need It)

> **Always implement things when you actually need them, never when you just foresee that you may need them.**

### Real-World Analogy
Packing a snow suit, snow shoes, and ice picks for a summer trip to Hawaii because "it might snow due to climate change" is wasteful. It wastes suitcase space and resources. Only pack what is needed for the trip at hand.

### Before (Bad) - Speculative Generalization
This class is designed to handle users, but incorporates inactive code for future caching, auditing, multi-database routing, and deletion queues that aren't requested yet.

```python
class UserManager:
    def __init__(self) -> None:
        self.users = {}
        # Speculative components for future feature requests
        self.audit_log = []
        self.cache_client = None  # To be implemented when we scale to 10M users
        self.backup_db = None     # For future failover support

    def add_user(self, user_id: str, name: str) -> None:
        self.users[user_id] = name
        self._log_transaction(user_id, "ADD")
        if self.cache_client:
            self._write_to_cache(user_id, name)

    def _log_transaction(self, user_id: str, action: str) -> None:
        # Placeholder audit trail
        self.audit_log.append((user_id, action))

    def _write_to_cache(self, user_id: str, name: str) -> None:
        pass
```

### After (Good) - Lean Implementation
Keep the class focused strictly on the current requirements.

```python
class UserManager:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, user_id: str, name: str) -> None:
        self.users[user_id] = name
```

---

## ⚖️ Summary Comparison

| Principle | Core Objective | Primary Danger of Violation |
| :--- | :--- | :--- |
| **DRY** | Prevent duplication of logic/knowledge. | High maintenance overhead; code inconsistencies when updating logic. |
| **KISS** | Avoid over-engineering; keep code readable. | Complex codebases that are difficult for new developers to understand. |
| **YAGNI** | Avoid writing unused speculative code. | Wasted development time; bloated classes full of dead or untested logic. |
