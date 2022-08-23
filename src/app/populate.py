"""
Read and Extract data from CSV files and load it into Database
"""
import logging
import sys
import pandas as pd
from pypika.terms import Parameter
from pypika.queries import Table, Query, QueryBuilder

sys.path.insert(0, '/src')

from utils.utils_postgres import set_connection, load_data

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)


class Extract:
    """
    Class to read and extract data from CSV files and insert it into Database
    """
    def __init__(self):
        self.postgres_conn = set_connection(LOGGER)
        self.customer_query = None
        self.products_query = None
        self.products_category_query = None
        self.order_items_query = None
        self.order_query = None
        self.seller_query = None

    def insert_customer_data(self):
        """
        Read the customer data the from csv file and insert it into the database

        :return:
        """
        # Read customer data from csv file into a pandas dataframe
        customer = pd.read_csv(filepath_or_buffer='/assets/olist_customers_dataset.csv')
        customer_tbl = Table('customer')

        customer_sql_obj: QueryBuilder = Query.into(customer_tbl).columns(
            customer_tbl.id, customer_tbl.customer_unique_id, customer_tbl.customer_zip_code_prefix,
            customer_tbl.customer_city, customer_tbl.customer_state
        ).insert(
            Parameter('%s'), Parameter('%s'), Parameter('%s'), Parameter('%s'),
            Parameter('%s')
        )

        load_data(customer, customer_sql_obj.get_sql(), self.postgres_conn, LOGGER)
        LOGGER.info("Inserted Customer Data")

    def insert_seller_data(self):
        """
        Read the seller data from the csv file and insert it into the database

        :return:
        """
        # Read seller data from csv file into a pandas dataframe
        seller_df = pd.read_csv(filepath_or_buffer='/assets/olist_sellers_dataset.csv')
        sellers_tbl = Table('seller')

        seller_sql_obj: QueryBuilder = Query.into(sellers_tbl).columns(
            sellers_tbl.id, sellers_tbl.seller_zip_code_prefix, sellers_tbl.seller_city,
            sellers_tbl.seller_state
        ).insert(
            Parameter('%s'), Parameter('%s'), Parameter('%s'), Parameter('%s')
        )

        load_data(seller_df, seller_sql_obj.get_sql(), self.postgres_conn, LOGGER)
        LOGGER.info("Inserted Seller Data")

    def insert_product_category_table_data(self):
        """
        Read the product category data from the csv file and insert it into the database

        :return:
        """
        # Read product category data from csv file into a pandas dataframe
        product_category_table_df = pd.read_csv(filepath_or_buffer=
                                                '/assets/product_category_name_translation.csv')
        product_category_tbl = Table('product_category_table')

        products_category_query_sql_obj: QueryBuilder = Query.into(product_category_tbl).columns(
            product_category_tbl.product_category_name,
            product_category_tbl.product_category_name_english
        ).insert(
            Parameter('%s'), Parameter('%s')
        )

        load_data(product_category_table_df, products_category_query_sql_obj.get_sql(),
                  self.postgres_conn, LOGGER)
        LOGGER.info("Inserted Product Category Data")

    def insert_product_data(self):
        """
        Read the product data from the csv file and insert it into the database

        :return:
        """
        # Read product data from csv file into a pandas dataframe
        products_df = pd.read_csv(filepath_or_buffer='/assets/olist_products_dataset.csv',
                                  usecols=["product_id", "product_category_name"], na_filter=True)
        products_tbl = Table('products')

        # Replace values in product category which are empty with 'Not yet classified'
        products_df['product_category_name'] = \
            products_df['product_category_name'].fillna('Not Yet Classified')

        products_sql_obj: QueryBuilder = Query.into(products_tbl).columns(
            products_tbl.id, products_tbl.product_category_name
        ).insert(
            Parameter('%s'), Parameter('%s')
        )

        load_data(products_df, products_sql_obj.get_sql(), self.postgres_conn, LOGGER)
        LOGGER.info("Inserted Product Data")

    def insert_order_data(self):
        """
        Read the order data from the csv file and insert it into the database

        :return:
        """
        # Read order data from csv file into a pandas dataframe
        order_df = pd.read_csv(filepath_or_buffer='/assets/olist_orders_dataset.csv',
                               usecols=["order_id", "customer_id", "order_status",
                                        "order_purchase_timestamp",
                                        "order_approved_at", "order_delivered_carrier_date",
                                        "order_delivered_customer_date"], na_filter=True
                               )

        # Replace pandas.Nan value with None
        order_df = order_df.where(pd.notnull(order_df), None)
        order_tbl = Table('order')

        order_sql_obj: QueryBuilder = Query.into(order_tbl).columns(
            order_tbl.id, order_tbl.customer_id, order_tbl.order_status,
            order_tbl.order_purchase_timestamp, order_tbl.order_approved_at,
            order_tbl.order_delivered_carrier_date, order_tbl.order_delivered_customer_date
        ).insert(
            Parameter('%s'), Parameter('%s'), Parameter('%s'), Parameter('%s'), Parameter('%s'),
            Parameter('%s'), Parameter('%s')
        )

        load_data(order_df, order_sql_obj.get_sql(), self.postgres_conn, LOGGER)
        LOGGER.info("Inserted Order Data")

    def insert_order_items_data(self):
        """
        Read the ordered items data from the csv file and insert it into the database

        :return:
        """
        # Read order items data from csv file into a pandas dataframe
        order_items_df = pd.read_csv(filepath_or_buffer='/assets/olist_order_items_dataset.csv',
                                     na_filter=True)

        # Delete the rows where order id is empty
        order_items_df.dropna(subset=["order_id"], inplace=True)

        # Delete 'shipping_limit_date' and 'order_item_id' as they are not required in the Database
        del order_items_df['shipping_limit_date']
        del order_items_df['order_item_id']
        order_items_tbl = Table('order_items')

        order_items_sql_obj: QueryBuilder = Query.into(order_items_tbl).columns(
            order_items_tbl.order_id, order_items_tbl.product_id, order_items_tbl.seller_id,
            order_items_tbl.price, order_items_tbl.freight_value
        ).insert(
            Parameter('%s'), Parameter('%s'), Parameter('%s'), Parameter('%s'), Parameter('%s')
        )

        load_data(order_items_df, order_items_sql_obj.get_sql(), self.postgres_conn, LOGGER)
        LOGGER.info("Inserted Order Items Data")

    def main(self):
        """

        :return:
        """
        self.insert_customer_data()
        self.insert_seller_data()
        self.insert_product_category_table_data()
        self.insert_product_data()
        self.insert_order_data()
        self.insert_order_items_data()


if __name__ == '__main__':
    EXTRACTOR_OBJ = Extract()
    EXTRACTOR_OBJ.main()
