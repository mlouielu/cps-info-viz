from pycps import get_asec, get_basic


BASIC_COLS = [
    "HEFAMINC",  # Family income
    "PEEDUCA",  # highest level of education
    "PESCHENR",  # last week enrolled in school?
    "PESEX",  # sex
    "PEMARITL",  # marital
    "PUDIS",  # disability status
    "PEDISPHY",  # serious difficulty walking or climbing
    "PEDISDRS",  # difficluty dressing or bathing
    "PEDISOUT",  # physical, mental, or emotional condition, difficulty doing errands
    "PRDISFLG",  # Any of these disability conditions?
    "PEHRUSL1",  # hours per week at main job
    "PEHRUSL2",  # hours per week at other job/jobs
    "PUABSOT",  # last week have job?
    "PEMJOT",  # more than one job?
    "PEMJNUM",  # totally, how many job?
    "PEIO1COW",  # 1st job class of worker code
    "PRDTIND1",  # 1st job detailed industry
    "PRDTOCC1",  # 1st job detailed occupation
    "PRMJIND1",  # 1st job major industry recode
    "PWSSWGT",  # person final weight
    "HRHHID",  # household identifier 1
    "HRHHID2",  # household identifier 2
]

ASEC_COLS = [
    "H_IDNUM",
    "HEFAMINC",  # family income from CPS recode
    "PEARNVAL",  # total persons earnings
    "PTOT_R",  # total person income recode
    "GTCBSASZ",  # metropolitan area size
    "GTCO",  # fips county code
    "GESTFIPS",  # fips state code
    "A_AGE",  # person age
    "A_SEX",  # person gender
    "A_WKSTAT",  # full/part-time status
    "WSAL_VAL",  # total wage & salary earnings (comb. ERN_VAL, i f ERN_SRCE=1, and WS_VAL)
    "DSAB_VAL",  # disability income
    "PRDTRACE",  # race
    "PEDISPHY",  # serious difficulty walking or climbing
    "PEDISDRS",  # difficluty dressing or bathing
    "PEDISOUT",  # physical, mental, or emotional condition, difficulty doing errands
    "HRSWK",  # hours per week at main job
    "INDUSTRY",
    "WEIND",
    "WEMIND",
    "OCCUP",
    "POCCU2",
    "WEMOCG",
    "LJCW",
]


def main():
    asec_start_year = 2019
    asec_end_year = 2023
    basic_start_year = 2019
    basic_end_year = 2024

    # Download ASEC
    for year in range(asec_start_year, asec_end_year + 1):
        print(year)
        asec = get_asec(year, ASEC_COLS)
        asec.to_pickle(f"data/asec_{year}.pkl")

    # Download Basic CPS
    # for year in range(basic_start_year, basic_end_year + 1):
    #     for month in range(1, 13):
    #         basic = get_basic(year, month, BASIC_COLS)
    #         basic.to_pickle(f"data/basic_{year}_{month}.pkl")


if __name__ == "__main__":
    main()
