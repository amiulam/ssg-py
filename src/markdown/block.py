from nodes.textnode import BlockType


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        stripped_block = block.strip()

        if stripped_block != "":
            filtered_blocks.append(stripped_block)

    return filtered_blocks


def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    if block.startswith(">"):
        is_quote = True
        for line in lines:
            if not line.startswith(">"):
                is_quote = False
                break
        if is_quote:
            return BlockType.QUOTE

    if block.startswith("- "):
        is_unordered = True
        for line in lines:
            if not line.startswith("- "):
                is_unordered = False
                break
        if is_unordered:
            return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        is_ordered = True
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                is_ordered = False
                break
            count += 1
        if is_ordered:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
