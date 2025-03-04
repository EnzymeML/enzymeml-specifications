---
hide:
  - navigation
  - toc
---

<div class="container">
  <div class="instructions">
    <p>
      The Validation Tool is designed to help you ensure your EnzymeML document is correct and consistent according to predefined rules and standards. It performs two main functions:
    </p>
    <ul>
      <li>
        <strong>Schema Validation:</strong>
        <br>
          Checks if the JSON structure matches the EnzymeML schema.
        </br>
      </li>
      <li>
        <strong>Consistency Checks:</strong>
        <br>
          Checks if the JSON is consistent with the EnzymeML specification.
        </br>
      </li>
    </ul>
    <p>
      For this, upload your EnzymeML JSON file using the file input below. The tool will then display the results of the validation and consistency checks.
      The Validation Tool is designed to help you ensure your EnzymeML document is correct and consistent according to predefined rules and standards. It performs two main functions:
    </p>
    <label for="file-input" class="upload-label">Choose File</label>
    <input type="file" id="file-input" class="upload-input" />

    <div class="responsive-wrapper">
      <div id="json-content-wrapper">
        <h3>JSON Content</h3>
        <div id="json-content"></div>
      </div>
    </div>

  </div>

  <div class="result-container">
    <div class="tabs">
      <button id="tab-validation" class="tab tab-active">
        <div class="tab-heading">
          <p>Schema Validation</p>
          <p id="valid-errors">
        </div>
      </button>
      <button id="tab-consistency" class="tab">
        <div class="tab-heading">
          <p>Consistency Checks</p>
          <p id="cons-errors">
        </div>
      </button>
    </div>
    <div id="validation" class="results results-active">
      <!-- Validation results will be displayed here -->
    </div>
    <div id="consistency" class="results">
      <!-- Consistency results will be displayed here -->
    </div>
  </div>
</div>

<link href="../css/treeviewer.css" rel="stylesheet" />
<script type="module">
  import validationPipeline from '../js/validation.js';

document.getElementById("file-input").addEventListener("change", validationPipeline);

document.getElementById("tab-validation").addEventListener("click", function () {
document.getElementById("validation").classList.add("results-active");
document.getElementById("consistency").classList.remove("results-active");
this.classList.add("tab-active");
document.getElementById("tab-consistency").classList.remove("tab-active");
});

document.getElementById("tab-consistency").addEventListener("click", function () {
document.getElementById("validation").classList.remove("results-active");
document.getElementById("consistency").classList.add("results-active");
this.classList.add("tab-active");
document.getElementById("tab-validation").classList.remove("tab-active");
});
</script>
