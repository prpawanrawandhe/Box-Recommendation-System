# Box Recommendation System – Test Cases

## 1. Testing Overview

- **Testing Type:** Manual Testing
- **Application:** Django-based Box Recommendation System
- **Dimensions Unit:** Centimeters (cm)
- **Weight Unit:** Kilograms (kg)
- **Cost Unit:** Indian Rupees (₹)

## 2. Available Box Details

| Box Name | Dimensions (L × W × H) | Max Weight | Cost |
|---|---|---:|---:|
| Small Box | 15 × 15 × 15 | 3 kg | ₹20 |
| Medium Box | 25 × 20 × 15 | 5 kg | ₹35 |
| Large Box | 30 × 25 × 20 | 10 kg | ₹50 |
| Extra Large Box | 40 × 30 × 25 | 15 kg | ₹75 |
| Heavy Duty Box | 50 × 40 × 30 | 25 kg | ₹120 |

## 3. Functional Test Cases

| Test ID | Length | Width | Height | Weight | Expected Result |
|---|---:|---:|---:|---:|---|
| TC01 | 10 | 10 | 10 | 2 | Small Box |
| TC02 | 20 | 15 | 10 | 4 | Medium Box |
| TC03 | 28 | 20 | 15 | 8 | Large Box |
| TC04 | 35 | 25 | 20 | 12 | Extra Large Box |
| TC05 | 45 | 35 | 25 | 20 | Heavy Duty Box |
| TC06 | 20 | 20 | 20 | 4 | Large Box |
| TC07 | 10 | 10 | 10 | 30 | No Suitable Box |
| TC08 | 60 | 50 | 40 | 5 | No Suitable Box |

## 4. Boundary Test Cases

| Test ID | Length | Width | Height | Weight | Expected Result |
|---|---:|---:|---:|---:|---|
| TC09 | 15 | 15 | 15 | 3 | Small Box |
| TC10 | 15 | 15 | 15 | 3.5 | Medium Box |
| TC11 | 50 | 40 | 30 | 25 | Heavy Duty Box |
| TC12 | 50.1 | 40 | 30 | 20 | No Suitable Box |

## 5. Input Validation Test Cases

| Test ID | Input | Expected Result |
|---|---|---|
| TC13 | Empty form submission | Browser should prevent submission |
| TC14 | Negative dimensions | Invalid input should be rejected |
| TC15 | Negative weight | Invalid input should be rejected |
| TC16 | Zero dimensions | Invalid input should be rejected |

## 6. Test Execution Summary

| Metric | Result |
|---|---|
| Total Test Cases | 16 |
| Passed | To be updated after execution |
| Failed | To be updated after execution |

**Note:** Expected results are based on the current box data and the application's box selection logic. Actual results and execution status should be recorded after testing each case.