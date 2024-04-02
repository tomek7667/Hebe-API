from bs4.element import Tag


class Order:
    def __init__(self, order_details_section: Tag, position: int):
        self.position = position
        self._tag = order_details_section
        [date, price, packs] = order_details_section.find_all(
            "span", class_="order-header__value"
        )
        self.date: str = date.text
        self.price: str = price.text
        self.packs: str = packs.text
        [order_id] = order_details_section.find_all(
            "span", class_="order-header__number-value"
        )
        self.id: str = order_id.text

    def __repr__(self) -> str:
        return f"Order({self.id}, {self.position}): {self.date} - {self.price}"
