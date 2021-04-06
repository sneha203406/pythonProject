import pandas as pd
from pandas import DataFrame
from pandas._testing import assert_frame_equal

from utilities.BaseClass import BaseClass


class TestComp(BaseClass):
    def test_dfComparison(self):
        log = self.getLogger()
        df1=pd.read_excel('C:\\Users\\KKRAJANN\\Documents\\demo.xlsx')
        # log.info("df1 : "+df1)
        df2=pd.read_excel('C:\\Users\\KKRAJANN\\Documents\\demo1.xlsx')
        # log.info("df1 : "+df2)

        # assert (df1.equals(df2))
        # assert_frame_equal(df1, df2,check_dtype=False)
        # assert(pd.DataFrame(df1, df2))
        # comparison_values = df1.values == df2.values
        # log.info("comparison_values"+comparison_values)


        # df = df1.merge(df2, how = 'outer' ,indicator=True)
        # print('****************')
        # print(df)
        # log.info(pd.testing.assert_frame_equal(df1, df2))
        print('_____________________________')
        log.info("Comparision ")
        log.info(pd.concat([df1, df2]).drop_duplicates(keep=False))
        print('_____________________________')
        pd.testing.assert_frame_equal(df1, df2)


        # log.info("first name is ")
