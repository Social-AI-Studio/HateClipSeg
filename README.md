# HateClipSeg

This repository contains the dataset developed for our paper:
***HateClipSeg: A Segment-Level Annotated Dataset for Fine-Grained Hate Video Detection***.

To advance research in **temporal hate speech detection**, we introduce **HateClipSeg**, a large-scale **multimodal dataset** with both **video-level** and **segment-level annotations**. The dataset includes over **11,714 video segments**, each labeled as either *Normal* or one or more of five *Offensive* categories:

* **Hateful**
* **Insulting**
* **Sexual**
* **Violent**
* **Self-Harm**

Each segment is also annotated with **explicit target victim labels**, enabling fine-grained and victim-aware detection tasks.

---

## 📊 Dataset Statistics

We ensured a **balanced distribution between Offensive and Normal segments**. Below is a summary of the label distribution:

**Table 1: Video-Level and Segment-Level Label Distribution**

| Label           | Video Count | Segment Count |
| --------------- | ----------- | ------------- |
| Hateful         | 194         | 2,363         |
| Insulting       | 280         | 2,920         |
| Sexual          | 69          | 372           |
| Violent         | 192         | 1,281         |
| Self-Harm       | 18          | 39            |
| **Offensive\*** | 380         | 5,223         |
| **Normal**      | 55          | 6,491         |

> \* Offensives may co-occur; video counts are non-exclusive.

---

## ✅ Annotation Process and Quality

We adopted a **three-stage annotation protocol**:
**Annotation → Discussion → Re-annotation**, which led to **high inter-annotator agreement**, especially at the segment level — an improvement over prior hate video datasets that lacked such detailed reporting.

**Table 2: Inter-Annotator Agreement (Krippendorff’s Alpha)**

| Annotation Task                | Before Discussion | After Discussion |
| ------------------------------ | ----------------- | ---------------- |
| Video-Level Offensive/Normal   | 0.791             | 0.817            |
| Segment-Level Offensive/Normal | 0.715             | 0.757            |
| Offensive Category Label       | 0.840             | 0.899            |
| Target Victim Label            | 0.716             | 0.721            |

---

## 🧠 Task Applications

With high-quality segment-level annotations, HateClipSeg enables the extension of hate video detection into the **temporal domain**. Specifically, it supports the development and benchmarking of tasks such as:

1. **Trimmed Video Classification**: Predict a single label for each pre-segmented clip.
2. **Temporal Video Localization**: Detect labels along with their start and end timestamps within untrimmed videos.
3. **Online Video Classification**: Perform real-time label prediction on streaming video.

<img src="Images/figure.png" alt="Diagram illustrating tasks" width="600"/>


---

## Dataset File Structure

### `Datset/video_level_annotation.csv`

This file contains **video-level annotations** with the following columns:

* **Video ID**: A combination of platform and the actual video ID.

  * Two platforms are included: `bitchute` and `youtube`, denoted as `bit` and `yt`, respectively.

* **Video-Level Label**: One or more labels selected from the list:
  `["normal", "hateful", "insulting", "sexual", "violence", "harm"]`

  * All labels except `"normal"` are considered **offensive categories** and allow **multi-label annotations**.

* **Target Victim**: One or more target groups mentioned in the video.

  * There are 21 predefined victim categories such as `"Woman"`, `"Man"`, `"Asian"`, `"Arab"`, `"Latino"`, `"Black"`, etc.
  * An `"Other"` category is included to cover unspecified targets.
  * Multiple selections are allowed.

## ✅ Example: `video_level_annotation.csv`

| Video ID      | Video-Level Label         | Target Victim |
| ------------- | -------------------------- | -------------- |
| yt\_abc123xyz | [hateful,insulting,violence] | [Woman,Black]    |

**Explanation**:

* `Video ID`: A YouTube video with ID `abc123xyz`
* `Video-Level Labels`: The video is labeled as **hateful**, **insulting**, and **violent**
* `Target Victims`: The offensive content targets **Women** and **Black** individuals

---

### `Datset/segment_level_annotation.csv`

This file contains **segment-level annotations** with the following columns:

* **Video ID**: Same format as described above.

* **Segment-Level Labels**: A list of N-length multi-hot vectors, where each vector represents the label(s) for a specific segment.

  * Label indices correspond to the following classes:
    `0: normal, 1: hateful, 2: insulting, 3: sexual, 4: violence, 5: harm`

* **Segment Timestamps**: A list of start and end timestamps for each of the N segments.


## ✅ Example: `segment_level_annotation.csv`

| Video ID      | Segment-Level Label                                                                | Segment Timestamp                                   |
| ------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------- |
| yt\_abc123xyz | \[ \[0,1,0,0,0,0], \[1,0,0,0,0,0], \[0,0,1,0,0,0], \[0,0,0,0,1,0], \[1,0,0,0,0,0] ] | \[ \[0,10], \[10,20], \[20,30], \[30,40], \[40,50] ] |

**Explanation**:

* `Segment-Level Labels`: Each segment is annotated with a 6-dimensional multi-hot vector where the index corresponds to:
  `0: normal, 1: hateful, 2: insulting, 3: sexual, 4: violence, 5: harm`
  So:

  * Segment 1 (0–10s): \[0,1,0,0,0,0] → **hateful**
  * Segment 2 (10–20s): \[1,0,0,0,0,0] → **normal**
  * Segment 3 (20–30s): \[0,0,1,0,0,0] → **insulting**
  * Segment 4 (30–40s): \[0,0,0,0,1,0] → **violence**
  * Segment 5 (40–50s): \[1,0,0,0,0,0] → **normal**

* `Segment Timestamps`: Each pair defines the start and end of a segment, in seconds.

---

### `lexicons.json`

This JSON file contains the **hate lexicons** used to search and identify relevant videos across platforms.

