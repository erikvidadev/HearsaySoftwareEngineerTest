About The App
   This FastAPI app is to create an HTTP service that accepts JSON input over HTTP,
   sorts arrays under specified keys, and returns a modified JSON output.

   
Summary of The Key Functionalities:
Input Format:
The app expects JSON input in a specific format, including a "data" field containing a dictionary of arrays and a "sortKeys" field containing a list of keys to sort.

Sorting:
The app sorts the arrays under the specified keys in the "data" field. It uses the provided "sortKeys" list to determine which arrays to sort.

Output Format:
The app returns the modified JSON, where the specified arrays are sorted.

HTTP API:
The app exposes an HTTP API endpoint at /sort to receive POST requests with the required JSON input.
