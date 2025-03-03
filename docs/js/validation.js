/**
 * Import the necessary functions from the wasm_validator module.
 */
import init, {
  validate_by_schema,
  check_consistency,
} from "https://unpkg.com/enzymeml-validator@0.1.0/enzymeml-validator.js";

console.log("Loading WASM module...");

/**
 * Handles the file upload event and triggers the validation pipeline.
 * @param {Event} event - The file upload event.
 */
export default function validationPipeline(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    document.querySelector(".upload-label").textContent = file.name;
    reader.onload = handleFileRead;
    reader.readAsText(file);
  }
}

/**
 * Handles the file read event and initiates the processing of the file content.
 * @param {Event} event - The file read event.
 */
function handleFileRead(event) {
  const valResElem = document.getElementById("validation");
  const consResElem = document.getElementById("consistency");
  const jsonContentElement = document.getElementById("json-content");
  const jsonContentWrapper = document.getElementById("json-content-wrapper");
  let consErrorCounter = document.getElementById("cons-errors");
  let validErrorCounter = document.getElementById("valid-errors");

  // Hide the JSON content wrapper and reset the upload label
  jsonContentWrapper.style.display = "none";
  jsonContentElement.innerHTML = "";

  // color: var(--md-default-fg-color)
  let uploadLabel = document.querySelector(".upload-label");
  uploadLabel.style.color = "var(--md-default-fg-color)";

  // Add JSON tree to jsonContentElement
  try {
    jsonTree.create(JSON.parse(event.target.result), jsonContentElement);
    jsonContentWrapper.style.display = "block";
  } catch (error) {
    let uploadLabel = document.querySelector(".upload-label");
    uploadLabel.textContent = "Not a JSON file: Click to upload another file.";
    uploadLabel.style.color = "red";
  }

  // Clean up the previous results
  valResElem.innerHTML = "";
  consResElem.innerHTML = "";

  // Clean up the error counters
  consErrorCounter.innerHTML = "";
  consErrorCounter.className = "";
  validErrorCounter.innerHTML = "";
  validErrorCounter.className = "";

  // Set tab to validation
  document.getElementById("validation").classList.add("results-active");
  document.getElementById("consistency").classList.remove("results-active");

  try {
    const json = JSON.parse(event.target.result);
    processFileContent(json, valResElem, consResElem);
  } catch (error) {
    document.getElementById("output").textContent =
      "Error parsing JSON: " + error.message;
  }
}

/**
 * Processes the file content by performing schema validation and consistency checks.
 * @param {Object} json - The JSON content of the file.
 * @param {HTMLElement} valResElem - The HTML element for displaying validation results.
 * @param {HTMLElement} consResElem - The HTML element for displaying consistency results.
 */
function processFileContent(json, valResElem, consResElem) {
  init().then(() => {
    // Perform a schema validation
    const valRes = validate_by_schema(JSON.stringify(json));

    if (valRes.errors.length > 0) {
      let validErrorCounter = document.getElementById("valid-errors");
      validErrorCounter.textContent = valRes.errors.length;
      validErrorCounter.className = "badge";
    }

    valResElem.appendChild(validationResultToDiv(valRes));

    // If valid, check consistency
    if (valRes.valid) {
      const consRes = check_consistency(JSON.stringify(json));

      if (consRes.errors.length > 0) {
        let consErrorCounter = document.getElementById("cons-errors");
        consErrorCounter.textContent = consRes.errors.length;
        consErrorCounter.className = "badge";
      }

      consResElem.appendChild(validationResultToDiv(consRes));
    }
  });
}

/**
 * Converts the validation result into an HTML div element.
 * @param {Object} valRes - The validation result.
 * @returns {HTMLDivElement} The div element containing the validation result.
 */
function validationResultToDiv(valRes) {
  const div = document.createElement("div");
  div.id = "validation-result";

  if (!valRes.valid) {
    valRes.errors.forEach((error) => {
      let message = error.message;
      let location = error.location;

      let errorElement = createErrorElement(location, message);

      div.appendChild(errorElement);
    });
  } else {
    let response = document.createElement("p");
    response.style.color = "green";
    response.style.margin = "0px";
    response.style.fontSize = "16px";
    response.textContent = "The EnzymeML document is valid!";
    div.appendChild(response);
  }

  return div;
}

/**
 * Transforms the validation errors into a key-value pair object.
 * @param {Array} errors - The array of validation errors.
 * @returns {Object} The transformed validation errors.
 */
function transformResult(errors) {
  let transformed = {};

  errors.forEach((error) => {
    transformed[error.location] = error.message;
  });

  return transformed;
}

/**
 * Converts the error message to HTML with highlighted text.
 * @param {string} message - The error message.
 * @returns {string} The HTML string with highlighted text.
 */
function messageToHTML(message) {
  const regex = /'([^']*)'/g;
  const modifiedStr = message.replace(
    regex,
    "<span class='highlight'>$1</span>",
  );
  return modifiedStr;
}

/**
 * Creates an HTML element for a validation error.
 * @param {string} location - The location of the validation error.
 * @param {string} message - The validation error message.
 * @returns {HTMLDivElement} The div element containing the validation error.
 */
function createErrorElement(location, message) {
  let errorElem = document.createElement("div");
  errorElem.id = "error-element";

  let locationElement = document.createElement("li");
  locationElement.className = "error-location";
  locationElement.textContent = location.substring(1);

  let messageElement = document.createElement("p");
  messageElement.className = "error-message";
  messageElement.innerHTML = messageToHTML(message);

  errorElem.appendChild(locationElement);
  errorElem.appendChild(messageElement);

  return errorElem;
}
