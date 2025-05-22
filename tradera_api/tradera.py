from dataclasses import dataclass
from enum import StrEnum, IntEnum
import httpx

BASE_URL = "https://www.tradera.com/"


class Sorting(StrEnum):
    best_hit = "Relevance"
    time_left = "TimeLeft"
    latest_added = "AddedOn"
    highest_price = "HighestPrice"
    lowest_price = "LowestPrice"
    highest_price_with_shipping = "HighestPriceWithShipping"
    lowest_price_with_shipping = "LowestPriceWithShipping"
    most_bids = "MostBids"
    least_bids = "LeastBids"
    popularity = "HighestWishListCount"


class AuctionType(StrEnum):
    all = "All"
    auction = "Auction"
    buy_now = "FixedPrice"


class Category(IntEnum):
    accessoarer = 1612
    antikt_design = 20
    barnartiklar = 1611
    barnklader_barnskor = 33
    barnleksaker = 302571
    biljetter_resor = 34
    bygg_verktyg = 32
    bocker_tidningar = 11
    datorer_tillbehor = 12
    dvd_videofilmer = 13
    fordon_batar_delar = 10
    ovrigt = 28
    foto_kameror_optik = 14
    frimarken = 15
    handgjort_konsthantverk = 36
    hem_hushall = 31
    hemelektronik = 17
    hobby = 18
    klockor = 19
    klader = 16
    konst = 23
    musik = 21
    mynt_sedlar = 22
    samlarsaker = 29
    skor = 1623
    skonhet = 340736
    smycken_adelstenar = 24
    sport_fritid = 25
    telefoni_tablets_wearables = 26
    tradgard_vaxter = 1605
    tv_spel_datorspel = 30
    vykort_bilder = 27


@dataclass
class TraderaAPI:
    _client: httpx.Client

    def __init__(self) -> None:
        client = httpx.Client()
        client.get(BASE_URL)
        self._client = client

    def search(
        self,
        query: str,
        category: Category | None = None,
        price: tuple[int, int] | None = None,
        auction_type: AuctionType = AuctionType.all,
        sorting: Sorting = Sorting.best_hit,
    ) -> dict:
        base_params: dict[str, bool | str | int] = {
            "automaticTranslationPreferred": True,
            "forceKeywordSearch": False,
            "includeFilters": False,
            "languageCodeIso2": "sv",
            "searchTypeVariantHint": "enrichemptysearchresult",
            "shippingCountryCodeIso2": "SE",
            "itemStatus": "unsold",
        }
        params = {
            **base_params,
            "query": query,
            "sortBy": sorting.value,
            "itemType": auction_type,
            **({"categoryId": category.value} if category else {}),
            **({"fromPrice": price[0], "toPrice": price[1]} if price else {}),
        }
        return self._client.post(
            f"{BASE_URL}/api/webapi/discover/web/independent-search", params=params
        ).json()
