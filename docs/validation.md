---
hide:
  - navigation
  - toc
---

<div class="container">
  <div class="instructions">
    <p>
      Upload an EnzymeML JSON file to check its validity. The Schema Validator checks if the EnzymeML Document conforms to the EnzymeML Schema. The Consistency Checker checks if the EnzymeML Document aligns with best practices. Warnings and Errors from the Consistency Checker are intended to communicate potential issues that may affect the interoperability of the document.
    </p>
    <p>
      Upload an EnzymeML JSON file using the file input below.
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
