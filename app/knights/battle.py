from app.knights.knight import Knight


class Battle:
    @staticmethod
    def fight(knights_config: dict) -> dict:
        knights = {
            name: Knight(data)
            for name, data in knights_config.items()
        }

        # Lancelot vs Mordred
        knights["lancelot"].take_damage(
            knights["mordred"].power - knights["lancelot"].protection
        )
        knights["mordred"].take_damage(
            knights["lancelot"].power - knights["mordred"].protection
        )

        # Arthur vs Red Knight
        knights["arthur"].take_damage(
            knights["red_knight"].power - knights["arthur"].protection
        )
        knights["red_knight"].take_damage(
            knights["arthur"].power - knights["red_knight"].protection
        )

        return {
            k.name: k.hp for k in knights.values()
        }
