# AI Usage Documentation

## 1. AI Tools Used

- ChatGPT (OpenAI)

## 2. Prompts Used

The following prompts were used during development:

1. How to create a Django-based box recommendation system?
2. How to retrieve box dimensions, weight capacity, and cost from Django models?
3. How to compare product dimensions with box dimensions while allowing rotation?
4. How to select the lowest-cost suitable box?
5. How to prevent form data resubmission when refreshing a Django page?
6. How to write automated test cases using Django TestCase?

## 3. Output Accepted

- Guidance for structuring the Django application.
- Suggestions for retrieving box data using Django ORM.
- Dimension sorting approach to support product rotation.
- Lowest-cost selection using Python's `min()` function.
- Guidance for writing automated Django tests.

## 4. Output Rejected or Modified

- Some suggested implementations were modified to match the existing project structure.
- Code suggestions were reviewed and adapted rather than blindly copied.
- Unnecessary implementation changes were avoided to keep the application simple.

## 5. Mistakes Found

- Initial template directory configuration was incorrect and required correction.
- The form refresh behavior needed further investigation to avoid POST resubmission.
- Some suggested code required adjustments to match the actual URL names and model fields.

## 6. Verification of Final Code

The application was manually tested with different product dimensions and weights.

Automated tests were also written using Django TestCase.

Command used:

`python manage.py test boxes`

Test execution result:

- Total automated tests: 5
- Passed: 5
- Failed: 0

The recommendation logic was verified for:
- Normal product dimensions.
- Weight capacity validation.
- Exact box dimension and weight limits.
- Products that do not fit in any available box.
- Selection of the suitable box with the lowest cost.

## 7. Conclusion

AI tools were used as development assistance for understanding concepts, debugging issues, and preparing test cases. The generated suggestions were reviewed, modified where necessary, and verified through manual and automated testing.
