CREATE TABLE balancewithdrawal (id bigint NOT NULL,
			amount VARCHAR ( 191 ),
            user_id bigint DEFAULT NULL,
            paymentmethod_id bigint DEFAULT NULL,
            deleted_at TIMESTAMP NULL DEFAULT NULL,
            created_at TIMESTAMP NULL DEFAULT NULL,
            updated_at TIMESTAMP NULL DEFAULT NULL
);
---fghgjhjh---
INSERT INTO balancewithdrawal VALUES(10, 300, 3, 7);

SELECT * FROM balancewithdrawal;