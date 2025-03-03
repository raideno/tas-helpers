import matplotlib.pyplot as plt

DEFAULT_FPS_VIDEO = 25
DEFAULT_TITLE = "Video Segmentation Representation"
LABELS_COLORS = {
    "grimpe": "#1f77b4",
    "chrono": "#ff7f0e",
    "lecture": "#2ca02c",
    "nothing": "#d62728",
    "brossage": "#9467bd"
}

def plot_video_segmentation(
    frames_labels: list[str],
    title: str = DEFAULT_TITLE,
    fps: int = DEFAULT_FPS_VIDEO,
):
    labels = list(set(frames_labels))
    
    color_map = {label: LABELS_COLORS.get(label, "#000000") for label in labels}

    grouped_labels = []
    current_label = frames_labels[0]
    start_frame = 0

    for i, label in enumerate(frames_labels):
        if label != current_label:
            grouped_labels.append((current_label, start_frame, i - 1))
            current_label = label
            start_frame = i
            
    grouped_labels.append((current_label, start_frame, len(frames_labels) - 1))

    plt.figure(figsize=(12, 2))
    
    xticks = []
    xtick_labels = []
    
    for label, start, end in grouped_labels:
        start_time = start / fps
        end_time = (end + 1) / fps
        plt.barh(
            y=0, 
            width=end_time - start_time,
            left=start_time,
            color=color_map[label],
            edgecolor="none",
            height=0.5
        )
        xticks.append(start_time)
        xtick_labels.append(f"{start_time:.1f}s")
    
    # Add the end of the last segment as a tick
    xticks.append(end_time)
    xtick_labels.append(f"{end_time:.1f}s")

    legend_elements = [plt.Line2D([0], [0], color=color_map[label], lw=4, label=label) for label in labels]
    
    plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 1), loc='upper left', title="Labels")

    plt.yticks([])
    plt.xticks(xticks, xtick_labels, rotation=90, fontsize=8)
    
    plt.xlabel("Time (seconds)")
    plt.title(title)
    
    plt.tight_layout()
    
    plt.show()