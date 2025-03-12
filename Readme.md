<p align="center">
  <img src="https://img.icons8.com/color/bell" width="100" alt="blue-cloud-image" style="filter: invert(32%) sepia(85%) saturate(3188%) hue-rotate(189deg) brightness(98%) contrast(95%);">
</p>
<p align="center">
    <h1 align="center">NotificationSender</h1>
</p>

<p align="center">
    <em>
    `NotificationSender` is a lightweight Python module designed to send notifications using the Pushbullet API. It simplifies the process of sending custom notifications with just a few lines of code.
    </em>
</p>

<p align="center"> 
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python"> 
  <img src="https://img.shields.io/badge/Pushbullet.py-00C853.svg?style=flat&logo=pushbullet&logoColor=white" alt="Pushbullet.py">
  <img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?style=flat&logo=visual-studio-code&logoColor=white" alt="VS Code">
</p>

<br>

## **Table of Contents**
- [Getting Started](#getting-started)
- [Function Parameters](#function-parameters)
- [Example Usage](#example-usage)
- [Environment Setup](#environment-setup)
- [Features](#features)
- [Using the Decorator](#using-the-decorator)

---

## **Overview**
`NotificationSender` is a python module made to quickly send notifications to your phone:

---

## **Getting Started**

### **Installation**
To use the `NotificationSender` module, add its directory to your Python path:

```python
import sys
sys.path.append(path_to_package)
from NotificationSender import SendNotif
```

### **Basic Usage**
After importing the `SendNotif` function, you can call it directly to send a notification:

```python
SendNotif()
```

This will send a test notification with default values.

---

## **Function Parameters**
The `SendNotif` function accepts the following arguments:

| **Argument** | **Type**    | **Default**           | **Description**                                                                 |
|--------------|-------------|-----------------------|---------------------------------------------------------------------------------|
| `title`      | `str`       | `"Test Notification"` | The title of the notification.                                                 |
| `body`       | `str`       | `"This is a test message from Python."` | The content of the notification.                                |
| `feedback`   | `bool`      | `False`              | If `True`, prints whether the notification was successfully sent.               |
| `API_KEY`    | `str`       | `None`               | Pushbullet API key. If `None`, it is retrieved from the `.env` file automatically. |

---

## **Example Usage**
Here’s an example of sending a custom notification with feedback:

```python
import sys
sys.path.append(r"c:\Users\tdrelangue\OneDrive\programmes\useful")
from NotificationSender import SendNotif

SendNotif(
    title="Custom Title",
    body="This is a custom notification message.",
    feedback=True
)
```

---

## **Using the Decorator**
The module also provides a `notify_on_completion` decorator, which automatically sends a notification when a function finishes execution—whether it succeeds or fails.

### **Decorator Usage**
You can use `notify_on_completion` to wrap any function:

```python
import time
import sys
sys.path.append(r"c:\Users\tdrelangue\OneDrive\programmes\useful")
from NotificationSender import SendNotif, notify_on_completion

@notify_on_completion
def example_function(success=True):
    """A test function to demonstrate the decorator."""
    if not success:
        raise ValueError("This is a test error!")
    time.sleep(2)
    return "Done!"

# Run the function
example_function(True)  # Sends a success notification
# example_function(False)  # Sends a failure notification
```

### **How It Works**
- ✅ If the function **completes successfully**, a notification is sent with the runtime.
- ❌ If the function **fails**, a notification is sent with the error message.
- ⚠️ The error **is still raised** so that it appears on-screen.

---

## **Environment Setup**
The API key for Pushbullet is stored securely in a `.env` file. Ensure your `.env` file contains the following:

```
API_KEY=your_pushbullet_api_key
```

---

## **Features**
- Easy to use and integrate.
- Supports custom titles and messages.
- Feedback to check notification status.
- Secure API key management using `.env`.
