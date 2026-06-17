# SkillCraft Technology Cyber Security Internship

## Task 02 - Image Encryption Tool

### Description

This project implements a simple Image Encryption and Decryption Tool using XOR-based pixel manipulation. The program encrypts image pixel values using a user-defined key and can decrypt the encrypted image by applying the same key again.

The project demonstrates basic image processing techniques and introduces the concept of reversible encryption using the XOR operation.

### Features

* Encrypt images using XOR encryption
* Decrypt encrypted images using the same key
* Supports PNG and JPG image formats
* User-defined encryption key
* Input validation for key values
* Automatic generation of processed image files

### Technologies Used

* Python 3
* Pillow (PIL) Library

### How It Works

Each pixel in an image consists of RGB (Red, Green, Blue) values.

Example:

Original Pixel:

```text
(255, 100, 50)
```

Key:

```text
200
```

Encrypted Pixel:

```text
(255 XOR 200, 100 XOR 200, 50 XOR 200)
```

The same key can be applied again to restore the original image because:

```text
(A XOR B) XOR B = A
```

### How to Run

Install Pillow:

```bash
pip install pillow
```

Run the program:

```bash
python image_encryptor.py
```

Enter:

* Image filename
* Encryption key (0–255)

The encrypted/decrypted image will be saved automatically.

### Sample Execution

Input:

```text
Enter image filename: sample.png
Enter key (0-255): 200
```

Output:

```text
Image processed successfully!
Saved as: sample_processed.png
```

### Learning Outcomes

* Image Processing Fundamentals
* Pixel Manipulation Techniques
* XOR Encryption Concepts
* Python File Handling
* Working with External Libraries
* Basic Cybersecurity Concepts

### Author

Nehanth Karnati
B.Tech CSE (Cybersecurity)
Bennett University

### Internship

SkillCraft Technology Cyber Security Internship
