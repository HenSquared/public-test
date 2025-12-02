# How Live Activities Work

Live Activities is an iOS feature introduced in iOS 16.1 that enables apps to display real-time, glanceable information on the iPhone Lock Screen and in the Dynamic Island (on iPhone 14 Pro and later models).

## Overview

Live Activities are designed to help users stay on top of tasks or events in real time, such as:
- Food delivery tracking
- Sports scores
- Ride-sharing status
- Workout progress
- Flight information
- Timer countdowns

## Key Components

### 1. ActivityKit Framework

Live Activities are powered by the **ActivityKit** framework. This framework provides the APIs to:
- Start a Live Activity
- Update a Live Activity
- End a Live Activity

```swift
import ActivityKit
```

### 2. Activity Attributes

To create a Live Activity, you need to define an `ActivityAttributes` struct that describes:
- **Static data**: Information that doesn't change during the activity (e.g., order ID, restaurant name)
- **Dynamic data (ContentState)**: Information that updates over time (e.g., delivery ETA, driver location)

```swift
struct DeliveryActivityAttributes: ActivityAttributes {
    // Static properties
    let orderNumber: String
    let restaurantName: String
    
    // Dynamic content that can be updated
    struct ContentState: Codable, Hashable {
        let driverName: String
        let estimatedDeliveryTime: Date
        let status: DeliveryStatus
    }
}
```

### 3. Widget Extension

Live Activities use **WidgetKit** for their UI. You create a Widget Extension that provides views for:
- **Lock Screen presentation**: The expanded view on the Lock Screen
- **Dynamic Island (compact)**: The minimal view in the Dynamic Island
- **Dynamic Island (expanded)**: The full expanded view when the user long-presses

```swift
struct DeliveryActivityWidget: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: DeliveryActivityAttributes.self) { context in
            // Lock Screen view
            DeliveryLockScreenView(context: context)
        } dynamicIsland: { context in
            DynamicIsland {
                // Expanded view regions
                DynamicIslandExpandedRegion(.leading) {
                    // Leading content
                }
                DynamicIslandExpandedRegion(.trailing) {
                    // Trailing content
                }
                DynamicIslandExpandedRegion(.bottom) {
                    // Bottom content
                }
            } compactLeading: {
                // Compact leading content
            } compactTrailing: {
                // Compact trailing content
            } minimal: {
                // Minimal view when multiple activities
            }
        }
    }
}
```

## Lifecycle of a Live Activity

### Starting a Live Activity

```swift
let attributes = DeliveryActivityAttributes(
    orderNumber: "12345",
    restaurantName: "Pizza Place"
)

let initialState = DeliveryActivityAttributes.ContentState(
    driverName: "John",
    estimatedDeliveryTime: Date().addingTimeInterval(1800),
    status: .preparing
)

do {
    let activity = try Activity.request(
        attributes: attributes,
        contentState: initialState,
        pushType: .token // Enables remote push notifications for this activity
    )
    
    // Get the push token to send to your server
    // Your server will use this token to send updates via APNs
    for await pushToken in activity.pushTokenUpdates {
        let tokenString = pushToken.map { String(format: "%02x", $0) }.joined()
        // Send tokenString to your server
        print("Push token: \(tokenString)")
    }
    
    print("Started activity: \(activity.id)")
} catch {
    print("Error starting activity: \(error)")
}
```

### Updating a Live Activity

There are two ways to update a Live Activity:

#### 1. Local Updates (from the app)

```swift
let updatedState = DeliveryActivityAttributes.ContentState(
    driverName: "John",
    estimatedDeliveryTime: Date().addingTimeInterval(900),
    status: .onTheWay
)

await activity.update(using: updatedState)
```

#### 2. Remote Push Notifications

Send updates from your server using Apple Push Notification service (APNs). Your server must:
1. Use the push token obtained when starting the activity
2. Send to APNs with the `apns-push-type: liveactivity` header
3. Use the `liveactivity` push type in the request

**APNs Request Headers:**
```
apns-push-type: liveactivity
apns-topic: <your-bundle-id>.push-type.liveactivity
apns-priority: 10
```

**Payload:**
```json
{
    "aps": {
        "timestamp": 1685952000,
        "event": "update",
        "content-state": {
            "driverName": "John",
            "estimatedDeliveryTime": 1685953800,
            "status": "onTheWay"
        },
        "alert": {
            "title": "Delivery Update",
            "body": "Your order is on the way!"
        }
    }
}
```

### Ending a Live Activity

```swift
let finalState = DeliveryActivityAttributes.ContentState(
    driverName: "John",
    estimatedDeliveryTime: Date(),
    status: .delivered
)

await activity.end(
    using: finalState,
    dismissalPolicy: .default // or .immediate, .after(date)
)
```

## Important Limitations

1. **Duration**: Live Activities can run for up to 8 hours. After that, the system may end them.

2. **Update Frequency**: Apple recommends updating no more than once per second to preserve battery life.

3. **Size Limits**: The ActivityAttributes and ContentState combined must be less than 4KB.

4. **Number of Activities**: An app can have multiple active Live Activities, but the system may limit display.

5. **Background Execution**: Apps cannot run code in the background just because they have a Live Activity running.

## Best Practices

1. **Keep UI Simple**: Live Activities should be glanceable. Show only essential information.

2. **Use Appropriate Update Frequency**: Update only when meaningful changes occur.

3. **Handle Stale Data**: Always consider the last update timestamp and display appropriate states for old data.

4. **Provide Clear Actions**: Include deep links to let users open relevant app screens when they tap the activity.

5. **End Activities Promptly**: End activities when the tracked event is complete to avoid user frustration.

## Requirements

- iOS 16.1 or later
- iPhone only (not available on iPad or Mac)
- Widget Extension in your app
- ActivityKit capability enabled in your app's entitlements

## Additional Resources

- [Apple's ActivityKit Documentation](https://developer.apple.com/documentation/activitykit)
- [Human Interface Guidelines for Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities)
- [WWDC 2022: Meet ActivityKit](https://developer.apple.com/videos/play/wwdc2022/10184/)
