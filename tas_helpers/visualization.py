import matplotlib.pyplot as plt

from typing import List, Dict, Tuple, Optional, Union

from tas_helpers.utils import frame_level_annotations_to_segment_level_annotations

class SegmentationVisualizer:
    def __init__(
        self,
        labels_values: List[str],
        labels_names: List[str] = None,
        labels_colors: List[str] = None,
    ):
        self.labels_values = labels_values or []
        self.labels_names = labels_names or labels_values or []
        self.labels_colors = labels_colors or SegmentationVisualizer.__derive_labels_colors(self.labels_values)
        
        assert len(self.labels_values) == len(self.labels_names)
        assert self.labels_colors is None or len(self.labels_values) == len(self.labels_colors)
    
    @staticmethod
    def __derive_labels_colors(labels_values: List[str]) -> List[str]:
        return [
            f"C{i}" for i in range(len(labels_values))
        ]
    
    def plot_segmentation(
        self,
        # --- --- ---
        frames_labels: List[str],
        fps: Optional[int] = None,
        # --- --- ---
        header: Optional[str] = None,
        footer: Optional[str] = None,
        # --- --- ---
        show_legend: bool = True,
        show_ticks: bool = True,
        bar_height: float = 0.5,
        figsize: Optional[Tuple[int, int]] = (12, 2),
        axis: Optional[plt.Axes] = None,
    ) -> Union[plt.Figure, plt.Axes]:
        if not frames_labels:
            raise ValueError("frames_labels cannot be empty")
            
        color_map = {label: color for label, color in zip(self.labels_values, self.labels_colors)}
        
        grouped_labels = frame_level_annotations_to_segment_level_annotations(frames_labels, fps)
        
        if axis is None:
            figure, axis = plt.subplots(figsize=figsize)
        else:
            figure = axis.figure
        
        xticks = []
        xtick_labels = []
        
        for label, start, end in grouped_labels:
            start_time = start / fps
            end_time = (end + 1) / fps
            axis.barh(
                y=0,
                width=end_time - start_time,
                left=start_time,
                color=color_map[label],
                height=bar_height
            )
            xticks.append(start_time)
            xtick_labels.append(f"{start_time:.1f}")
        
        if grouped_labels:
            _, _, last_end = grouped_labels[-1]
            end_time = (last_end + 1) / fps
            xticks.append(end_time)
            xtick_labels.append(f"{end_time:.1f}")

        if show_legend:
            legend_elements = [
                plt.Line2D([0], [0], color=color_map[label_value], lw=4, label=label_name) 
                for label_value, label_name in zip(self.labels_values, self.labels_names)
            ]
            axis.legend(handles=legend_elements, loc="upper right")

        axis.set_yticks([])
        if show_ticks:
            axis.set_xticks(xticks)
            axis.set_xticklabels(xtick_labels, rotation=90, fontsize=8)
        else:
            axis.set_xticks([])
        
        axis.set_title(header)
        axis.set_xlabel(footer)
        
        plt.tight_layout()
        
        return axis if axis is not None else figure