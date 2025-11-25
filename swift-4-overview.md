# Swift 4 Overview

Swift 4 was officially released on **September 19, 2017**, and introduced several important features focused on source code robustness, stability, and ease of migration from Swift 3.

## Release Details

- **Official Release Date:** September 19, 2017
- **First Shown:** WWDC 2017
- **Major Goals:** Improve source stability for Swift 3 code, work toward ABI (Application Binary Interface) stability for the standard library, and introduce new language features with minimal source-breaking changes.

## Main Features

### 1. Source Compatibility

Swift 4 aimed to ease migration from Swift 3 with dual compatibility modes:

- **Swift 3.2 Mode:** Allows the majority of Swift 3.x code to compile unchanged.
- **Swift 4.0 Mode:** Enables all new language and API features, sometimes requiring modest migration efforts.

### 2. Improved String Handling

Strings became more efficient, Unicode-correct, and easier to use:

- Strings now conform to `Collection`, so you can iterate over a string character-by-character.
- Support for substrings with improved performance.
- Multi-line string literals using triple quotes (`"""..."""`), making multi-line string creation more readable and maintainable.

**Example:**
```swift
let multilineString = """
    This is a multi-line
    string literal in Swift 4.
    It preserves formatting.
    """
```

### 3. Archival and Serialization (Codable)

Introduction of the `Codable` protocol, making encoding and decoding data types (such as to/from JSON or property lists) automatic and type-safe. This drastically reduced boilerplate code for serialization.

**Example:**
```swift
struct Person: Codable {
    var name: String
    var age: Int
}

// Encoding to JSON
let person = Person(name: "John", age: 30)
let encoder = JSONEncoder()
let jsonData = try encoder.encode(person)

// Decoding from JSON
let decoder = JSONDecoder()
let decodedPerson = try decoder.decode(Person.self, from: jsonData)
```

### 4. KeyPath Improvements

Type-safe key-value coding with enhanced key paths. Key paths in Swift 4 enable dynamic property access with compile-time checking, helping eliminate runtime errors typical in Objective-C key-value coding.

**Example:**
```swift
struct User {
    var name: String
    var email: String
}

let nameKeyPath = \User.name
let user = User(name: "Alice", email: "alice@example.com")
print(user[keyPath: nameKeyPath]) // Prints "Alice"
```

### 5. Dictionary & Set Enhancements

Dictionaries and sets gained utility improvements:

- `mapValues` for transforming values while preserving keys.
- Grouping initializer for dictionaries.
- Subscript with default value to avoid optionals.
- Custom collections for dictionary keys and values.

**Example:**
```swift
// Default value for subscript
var scores = ["Alice": 95, "Bob": 87]
let charlieScore = scores["Charlie", default: 0] // Returns 0 instead of nil

// Grouping initializer
let names = ["Alice", "Bob", "Anna", "Brian"]
let grouped = Dictionary(grouping: names, by: { $0.first ?? Character(" ") })
// ["A": ["Alice", "Anna"], "B": ["Bob", "Brian"]]
```

### 6. Collections Updates

- One-sided ranges for easier slicing
- Generic subscripts
- Introduction of methods like `MutableCollection.swapAt(_:_:)`

**Example:**
```swift
let numbers = [1, 2, 3, 4, 5]
let fromSecond = numbers[1...] // [2, 3, 4, 5] - from index 1 to end
let upToThird = numbers[..<3]  // [1, 2, 3] - indices 0, 1, 2 (first 3 elements)
```

### 7. Access Control and Protocol Enhancements

- Improvements in protocol-oriented programming
- Protocol-oriented integers
- Limitation of automatic `@objc` inference for cleaner Swift code

### 8. Other Language Updates

- Strict memory access rules (`Enforce Exclusive Access to Memory`)
- Enhancements in numeric types
- Better bridging with `NSNumber`

## Migration and Compatibility

Swift 4 prioritized a smoother migration from Swift 3, with the Xcode migration tool handling most changes automatically. Mixed-mode projects could coexist, gradually allowing modules to adopt Swift 4 at their own pace.

## Conclusion

Swift 4 was a crucial step toward stabilizing the language and its ecosystem, ensuring long-term viability for app and system developers on Apple platforms. Its flagship features—like the `Codable` protocol, multi-line strings, improved collections, and backward compatibility—made Swift code more expressive and safer, while reducing the cost of migrating legacy projects.

## References

- [Swift 4.0 Released! | Swift.org](https://www.swift.org/blog/swift-4.0-released/)
- [What's new in Swift 4.0 | Hacking With Swift](https://www.hackingwithswift.com/swift4)
- [Swift 4 Release Process | Swift.org](https://www.swift.org/blog/swift-4.0-release-process/)
