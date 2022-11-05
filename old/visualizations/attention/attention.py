import html
import json
from pathlib import Path
from typing import List, Optional

import numpy as np
from pysvelte import build, html_wrapper


def AttentionPatterns(
    tokens: List[str],
    attention: np.ndarray,
    # info_weighted: Optional[np.ndarray] = None,
    # head_labels: Optional[str] = None
) -> html_wrapper.Html:
    """Visualize the attention patterns for multiple attention heads.

    This component is used to visualize attention patterns from a Transformer
    self-attention module. A previous version of this component was used to
    generate the attention explorer seen here:
    https://transformer-circuits.pub/2021/framework/2L_HP_normal.html
    and linked to from the Anthropic paper here:
    https://transformer-circuits.pub/2021/framework/index.html

    Args:
      tokens: a list of of strings representing tokens
      attention: A [N, N, H] array representing attention probabilities,
        where N is the number of tokens and H is the number of heads
        (or analogous value like number of NMF factors).

        Attention weights are expected to be in [0, 1].
    """
    #   info_weighted: (optional) A [N, N, H] array represented
    #     re-weighted attention patterns. If provided, the component
    #     will allow toggling between this pattern and the standard
    #     pattern.

    #   head_labels: human readable labels for heads. Optional.

    # Validate data
    assert (
        len(tokens) == attention.shape[0]
    ), "tokens and activations must be same length"
    assert (
        attention.shape[0] == attention.shape[1]
    ), "first two dimensions of attention must be equal"
    assert attention.ndim == 3, "attention must be 3D"
    # if head_labels is not None:
    #     assert (
    #         len(head_labels) == attention.shape[-1]
    #     ), "head_labels must correspond to number of attention heads"
    # if info_weighted is not None:
    #     assert (
    #         attention.shape == info_weighted.shape
    #     ), "info_weighted must be the same shape as attention"

    # Encode twice (as Jupyter decodes once before printing)
    escaped_tokens = [html.escape(html.escape(token)) for token in tokens]

    props: dict = {
        "tokens": json.dumps(escaped_tokens),
        "attention": json.dumps(attention.tolist())
    }
    
    # if info_weighted:
    #     props.info_weighted = json.dumps(  # type: ignore
    #         info_weighted.tolist())

    # if head_labels:
    #     props.head_labels = json.dumps(head_labels)  # type: ignore

    return build.render(
        Path(__file__).parent / "AttentionPatterns.tsx",
        **props
    )
