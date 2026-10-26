
USE FoodDeliveryETA;
GO

SELECT
    COUNT(*) AS Total_Orders,
    ROUND(
        AVG(CAST(Time_taken_min AS FLOAT)), 2
    ) AS Average_Delivery_Minutes,
    MIN(CAST(Time_taken_min AS FLOAT)) AS Minimum_Delivery_Minutes,
    MAX(CAST(Time_taken_min AS FLOAT)) AS Maximum_Delivery_Minutes,
    SUM(
        CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34
            THEN 1 ELSE 0
        END
    ) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN CAST(Time_taken_min AS FLOAT) > 34
                THEN 1 ELSE 0
            END
        ) / COUNT(*), 2
    ) AS Delayed_Percentage
FROM dbo.delivery_data;


-- Query 2: Delivery performance by order type

SELECT
    Type_of_order,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(CAST(Time_taken_min AS FLOAT)), 2) AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
GROUP BY Type_of_order
ORDER BY Delayed_Percentage DESC;


-- Query 3: Delivery delays by vehicle condition

SELECT
    Vehicle_condition,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
GROUP BY Vehicle_condition
ORDER BY Delayed_Percentage DESC;


-- Query 4: Delivery delays by order hour

SELECT
    Order_Hour,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Order_Hour IS NOT NULL
GROUP BY Order_Hour
ORDER BY Delayed_Percentage DESC;


-- Query 5: Delivery delays by distance category

SELECT
    CASE
        WHEN Distance_km < 5 THEN '0-5 km'
        WHEN Distance_km < 10 THEN '5-10 km'
        WHEN Distance_km < 15 THEN '10-15 km'
        ELSE '15+ km'
    END AS Distance_Category,
    COUNT(*) AS Total_Orders,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Distance_km IS NOT NULL
GROUP BY
    CASE
        WHEN Distance_km < 5 THEN '0-5 km'
        WHEN Distance_km < 10 THEN '5-10 km'
        WHEN Distance_km < 15 THEN '10-15 km'
        ELSE '15+ km'
    END
ORDER BY MIN(Distance_km);


-- Query 6: Delivery delays by weather condition

SELECT
    Weatherconditions,
    COUNT(*) AS Total_Orders,
    ROUND(
        AVG(CAST(Time_taken_min AS FLOAT)), 2
    ) AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Weatherconditions IS NOT NULL
GROUP BY Weatherconditions
ORDER BY Delayed_Percentage DESC;


-- Query 7: Delivery delays by traffic density

SELECT
    Road_traffic_density,
    COUNT(*) AS Total_Orders,
    ROUND(
        AVG(CAST(Time_taken_min AS FLOAT)), 2
    ) AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Road_traffic_density IS NOT NULL
GROUP BY Road_traffic_density
ORDER BY Delayed_Percentage DESC;


-- Query 8: Delivery delays by vehicle type

SELECT
    Type_of_vehicle,
    COUNT(*) AS Total_Orders,
    ROUND(
        AVG(CAST(Time_taken_min AS FLOAT)), 2
    ) AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Type_of_vehicle IS NOT NULL
GROUP BY Type_of_vehicle
ORDER BY Delayed_Percentage DESC;


-- Query 9: Delivery delays by festival status

SELECT
    Festival,
    COUNT(*) AS Total_Orders,
    ROUND(
        AVG(CAST(Time_taken_min AS FLOAT)), 2
    ) AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Festival IS NOT NULL
GROUP BY Festival
ORDER BY Delayed_Percentage DESC;


-- Query 10: Delivery delays by city

SELECT
    City,
    COUNT(*) AS Total_Orders,
    ROUND(
        AVG(CAST(Time_taken_min AS FLOAT)), 2
    ) AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE City IS NOT NULL
GROUP BY City
ORDER BY Delayed_Percentage DESC;



-- Query 11: Delivery delays by distance category

SELECT
    CASE
        WHEN Distance_km < 5 THEN '0-5 km'
        WHEN Distance_km < 10 THEN '5-10 km'
        WHEN Distance_km < 15 THEN '10-15 km'
        ELSE '15+ km'
    END AS Distance_Category,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(CAST(Time_taken_min AS FLOAT)), 2)
        AS Average_Delivery_Minutes,
    SUM(CASE
        WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
        ELSE 0
    END) AS Delayed_Orders,
    ROUND(
        100.0 * SUM(CASE
            WHEN CAST(Time_taken_min AS FLOAT) > 34 THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS Delayed_Percentage
FROM dbo.delivery_data
WHERE Distance_km IS NOT NULL
GROUP BY
    CASE
        WHEN Distance_km < 5 THEN '0-5 km'
        WHEN Distance_km < 10 THEN '5-10 km'
        WHEN Distance_km < 15 THEN '10-15 km'
        ELSE '15+ km'
    END
ORDER BY MIN(Distance_km);
