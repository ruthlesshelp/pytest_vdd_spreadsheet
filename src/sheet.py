class Sheet:
    def get(self, cell_ref: str) -> str:
        """Get the calculated value of a cell."""
        return ""

    def put(self, cell_ref: str, value: str) -> None:
        """Set the value of a cell."""
        raise NotImplementedError("Sheet.put() not implemented")

    def get_literal(self, cell_ref: str) -> str:
        """Get the raw/literal value of a cell for editing."""
        raise NotImplementedError("Sheet.get_literal() not implemented")
