import ritual_runner


def test_list_scrolls_returns_files():
    scrolls = ritual_runner.list_scrolls()
    assert isinstance(scrolls, list)
    assert len(scrolls) >= 1


def test_display_scroll_handles_missing_file():
    # Should not raise an exception when file does not exist
    result = ritual_runner.display_scroll('no_such_scroll.sql')
    assert result is None
