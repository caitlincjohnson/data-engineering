view: global_sales {
  sql_table_name: "DEMO"."GLOBAL_SALES" ;;

  dimension: category {
    type: string
    sql: ${TABLE}."Category" ;;
  }
  dimension: city {
    type: string
    sql: ${TABLE}."City" ;;
  }
  dimension: country {
    type: string
    map_layer_name: countries
    sql: ${TABLE}."Country" ;;
  }
  dimension: customer_id {
    type: string
    sql: ${TABLE}."Customer ID" ;;
  }
  dimension: customer_name {
    type: string
    sql: ${TABLE}."Customer Name" ;;
  }
  dimension: discount {
    type: number
    sql: ${TABLE}."Discount" ;;
  }
  dimension: market {
    type: string
    sql: ${TABLE}."Market" ;;
  }
  dimension_group: order {
    type: time
    timeframes: [raw, date, week, month, quarter, year]
    convert_tz: no
    datatype: date
    sql: ${TABLE}."Order Date" ;;
  }
  dimension: order_id {
    type: string
    sql: ${TABLE}."Order ID" ;;
  }
  dimension: order_priority {
    type: string
    sql: ${TABLE}."Order Priority" ;;
  }
  dimension: postal_code {
    type: string
    sql: ${TABLE}."Postal Code" ;;
  }
  dimension: product_id {
    type: string
    sql: ${TABLE}."Product ID" ;;
  }
  dimension: product_name {
    type: string
    sql: ${TABLE}."Product Name" ;;
  }
  dimension: profit {
    type: number
    sql: ${TABLE}."Profit" ;;
  }
  dimension: quantity {
    type: number
    sql: ${TABLE}."Quantity" ;;
  }
  dimension: region {
    type: string
    sql: ${TABLE}."Region" ;;
  }
  dimension: row_id {
    type: number
    sql: ${TABLE}."Row ID" ;;
  }
  dimension: sales {
    type: number
    sql: ${TABLE}."Sales" ;;
  }
  dimension: segment {
    type: string
    sql: ${TABLE}."Segment" ;;
  }
  dimension_group: ship {
    type: time
    timeframes: [raw, date, week, month, quarter, year]
    convert_tz: no
    datatype: date
    sql: ${TABLE}."Ship Date" ;;
  }
  dimension: ship_mode {
    type: string
    sql: ${TABLE}."Ship Mode" ;;
  }
  dimension: shipping_cost {
    type: number
    sql: ${TABLE}."Shipping Cost" ;;
  }
  dimension: state {
    type: string
    sql: ${TABLE}."State" ;;
  }
  dimension: subcategory {
    type: string
    sql: ${TABLE}."Sub-Category" ;;
  }
  measure: count {
    type: count
    drill_fields: [customer_name, product_name]
  }
}
