# test-web-accessibility
This action is used for testing website accessibility and generating report for any decision making.

# Usage

```
      - name: Test Websites
        id: test-web
        uses: harryzhou1987/test-web-accessibility@v0.0.1
        with:
          URLs: |
            "https://google.com"
            "https://github.com"
            "https://github.com/harryzhou1987/test-web-accessibility"
          ERROR_THRESHOLD: 1
        
```
- **URLs**: List of URLs to be tested.
- **ERROR_THRESHOLD**: Action fails when number of errors exceeds the threshold. Default value is 0. 

# Test Result Example:
```
Test Report - 2024-07-10
Success:2, Redirects:0, Errors:1

Success:
 - https://google.com
 - https://github.com

Redirects:

Errors:
 - https://github.com/harryzhou1987/test-web-accessibilit
```