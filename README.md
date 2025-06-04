# HateClipSeg

This repository provides the dataset introduced in our paper:
**HateClipSeg: A Segment-Level Annotated Dataset for Fine-Grained Hate Video Detection**.

To advance research in **temporal hate speech detection**, we present **HateClipSeg** — a large-scale **multimodal dataset** featuring both **video-level** and **segment-level annotations**. It contains over **11,714 video segments**, each labeled as *Normal* or one or more of five *Offensive* categories:

* **Hateful**
* **Insulting**
* **Sexual**
* **Violent**
* **Self-Harm**

Additionally, each segment is annotated with **explicit target victim labels**, enabling nuanced, victim-aware detection tasks.

---

## 📊 Dataset Statistics

We maintained a **balanced distribution between Offensive and Normal segments**. Summary:

| Label           | Video Count | Segment Count |
| --------------- | ----------- | ------------- |
| Hateful         | 194         | 2,363         |
| Insulting       | 280         | 2,920         |
| Sexual          | 69          | 372           |
| Violent         | 192         | 1,281         |
| Self-Harm       | 18          | 39            |
| **Offensive\*** | 380         | 5,223         |
| **Normal**      | 55          | 6,491         |

> \* Offensive categories may co-occur; video counts are non-exclusive.

---

## ✅ Annotation Process and Quality

Our **three-stage annotation protocol** — **Annotation → Discussion → Re-annotation** — yields high inter-annotator agreement, especially at the segment level, improving upon prior hate video datasets that lacked detailed agreement reporting.

| Annotation Task                | Before Discussion | After Discussion |
| ------------------------------ | ----------------- | ---------------- |
| Video-Level Offensive/Normal   | 0.791             | 0.817            |
| Segment-Level Offensive/Normal | 0.715             | 0.757            |
| Offensive Category Label       | 0.840             | 0.899            |
| Target Victim Label            | 0.716             | 0.721            |

(*Krippendorff’s Alpha*)

---

## 🧠 Task Applications

Thanks to high-quality segment-level labels, HateClipSeg supports advancing hate video detection into the **temporal domain**, enabling:

1. **Trimmed Video Classification**
   Predict a single label per pre-segmented clip.

2. **Temporal Video Localization**
   Detect labels with precise start and end timestamps in untrimmed videos.

3. **Online Video Classification**
   Real-time prediction on streaming video.

<img src="Images/figure.png" alt="Diagram illustrating tasks" width="600"/>

---

## Dataset File Structure

### `Dataset/video_level_annotation.csv`

Contains **video-level annotations** with columns:

* **Video ID**: Combines platform and video identifier.
  Platforms:

  * `bitchute` (prefix `bit`)
  * `youtube` (prefix `yt`)

* **Video-Level Label**: One or more labels from:
  `["normal", "hateful", "insulting", "sexual", "violence", "harm"]`
  All except `"normal"` are **offensive categories** and support multi-labels.

* **Target Victim**: One or more target groups mentioned, chosen from 21 predefined categories such as `"Woman"`, `"Man"`, `"Asian"`, `"Arab"`, `"Latino"`, `"Black"`, plus `"Other"`. Multiple selections allowed.

#### Example

| Video ID      | Video-Level Label               | Target Victim   |
| ------------- | ------------------------------- | --------------- |
| yt\_abc123xyz | \[hateful, insulting, violence] | \[Woman, Black] |

* A YouTube video (`abc123xyz`) labeled as hateful, insulting, and violent, targeting Women and Black individuals.

---

### `Dataset/segment_level_annotation.csv`

Contains **segment-level annotations** with columns:

* **Video ID**: Same format as above.

* **Segment-Level Labels**: List of multi-hot vectors for each segment.
  Label indices:
  `0: normal, 1: hateful, 2: insulting, 3: sexual, 4: violence, 5: harm`

* **Segment Timestamps**: List of `[start, end]` timestamps per segment.

#### Example

| Video ID      | Segment-Level Label                                                               | Segment Timestamp                                  |
| ------------- | --------------------------------------------------------------------------------- | -------------------------------------------------- |
| yt\_abc123xyz | \[\[0,1,0,0,0,0], \[1,0,0,0,0,0], \[0,0,1,0,0,0], \[0,0,0,0,1,0], \[1,0,0,0,0,0]] | \[\[0,10], \[10,20], \[20,30], \[30,40], \[40,50]] |

* Segment labels correspond to:

  * 0–10s: hateful
  * 10–20s: normal
  * 20–30s: insulting
  * 30–40s: violence
  * 40–50s: normal

---

### lexicons.json

This JSON file contains the **hate lexicons** used to search and identify relevant videos across platforms.
