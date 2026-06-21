from patterns.behavioral.state.pattern import Document, DraftState


def test_state_transitions() -> None:
    """Verifies that the document transitions through states and returns appropriate content."""
    # Starts in Draft
    doc = Document(DraftState())
    assert doc.render() == "Draft: Rendering editor workspace views."

    # Publish draft -> transitions to Moderation
    res1 = doc.publish()
    assert res1 == "Draft: Moved document to Moderation."
    assert doc.render() == "Moderation: Rendering admin review workspace."

    # Publish moderation -> transitions to Published
    res2 = doc.publish()
    assert res2 == "Moderation: Moved document to Published."
    assert doc.render() == "Published: Rendering public reading views."

    # Publish published -> stays in Published
    res3 = doc.publish()
    assert res3 == "Published: Document is already published."
    assert doc.render() == "Published: Rendering public reading views."
