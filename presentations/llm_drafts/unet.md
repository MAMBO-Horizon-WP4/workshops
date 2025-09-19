title: "Attention U-Net for Remote Sensing"
format: revealjs
editor: visual

---

## What is Attention U-Net?

- Extension of U-Net for image segmentation
- Adds attention gates to focus on relevant regions
- Useful for noisy or complex remote sensing data

---

## Architecture Overview

- **Encoder**: Extracts features from input image
- **Decoder**: Reconstructs segmented output
- **Skip Connections**: Preserve spatial details
- **Attention Gates**: Highlight important features, suppress irrelevant ones

## 🌿 Biodiversity-Relevant Labels for Attention U-Net

| Model Component       | Biodiversity-Relevant Label or Analogy                              |
|-----------------------|----------------------------------------------------------------------|
| **Input Image**       | Satellite or drone image of a forest, wetland, or coral reef         |
| **Encoder Layers**    | Feature extraction: vegetation texture, canopy density, water edges  |
| **Bottleneck**        | Compressed representation of ecological features                     |
| **Attention Gates**   | Focus on species habitats, deforestation zones, or invasive patches  |
| **Skip Connections**  | Preserve spatial details like river boundaries or tree clusters      |
| **Decoder Layers**    | Reconstruct segmented map: habitat zones, land cover types           |
| **Output Segmentation** | Labeled map showing forest types, biodiversity hotspots, etc.     |

---

## Why It Matters

- Improves segmentation of land cover, habitats
- Filters out noise (e.g., shadows, clouds)
- Enhances biodiversity monitoring from satellite data

---

## Real-World Example

- Used in building extraction from high-res imagery
- Attention gates improved boundary detection
- Applicable to forest mapping, species habitat delineation

---

## Summary

- Attention U-Net = U-Net + smarter focus
- Ideal for complex remote sensing tasks
- Boosts precision in biodiversity applications

