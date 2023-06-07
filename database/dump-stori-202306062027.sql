--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-06-06 20:27:04 CST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3633 (class 1262 OID 16390)
-- Name: stori; Type: DATABASE; Schema: -; Owner: -
--
--CREATE DATABASE stori WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = icu LOCALE = 'en_US.UTF-8' ICU_LOCALE = 'en-US';


\connect stori

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA IF NOT EXISTS public;


--
-- TOC entry 3634 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16406)
-- Name: balance; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE IF NOT EXISTS public.balance (
    id integer NOT NULL,
    total double precision NOT NULL,
    debit_average double precision NOT NULL,
    credit_average double precision NOT NULL
);


--
-- TOC entry 216 (class 1259 OID 16405)
-- Name: balance_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.balance_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3635 (class 0 OID 0)
-- Dependencies: 216
-- Name: balance_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.balance_id_seq OWNED BY public.balance.id;


--
-- TOC entry 219 (class 1259 OID 16427)
-- Name: monthly_count; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE  IF NOT EXISTS public.monthly_count (
    id integer NOT NULL,
    month character varying(9) NOT NULL,
    year integer NOT NULL,
    transaction_count integer NOT NULL
);


--
-- TOC entry 218 (class 1259 OID 16426)
-- Name: monthly_count_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.monthly_count_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3636 (class 0 OID 0)
-- Dependencies: 218
-- Name: monthly_count_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.monthly_count_id_seq OWNED BY public.monthly_count.id;


--
-- TOC entry 215 (class 1259 OID 16399)
-- Name: transactions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE IF NOT EXISTS public.transactions (
    id integer NOT NULL,
    transaction integer NOT NULL,
    transaction_date date
);


--
-- TOC entry 214 (class 1259 OID 16398)
-- Name: transactions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.transactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 3637 (class 0 OID 0)
-- Dependencies: 214
-- Name: transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.transactions_id_seq OWNED BY public.transactions.id;


--
-- TOC entry 3472 (class 2604 OID 16409)
-- Name: balance id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.balance ALTER COLUMN id SET DEFAULT nextval('public.balance_id_seq'::regclass);


--
-- TOC entry 3473 (class 2604 OID 16430)
-- Name: monthly_count id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monthly_count ALTER COLUMN id SET DEFAULT nextval('public.monthly_count_id_seq'::regclass);


--
-- TOC entry 3471 (class 2604 OID 16402)
-- Name: transactions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions ALTER COLUMN id SET DEFAULT nextval('public.transactions_id_seq'::regclass);


--
-- TOC entry 3625 (class 0 OID 16406)
-- Dependencies: 217
-- Data for Name: balance; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.balance (id, total, debit_average, credit_average) FROM stdin;
\.


--
-- TOC entry 3627 (class 0 OID 16427)
-- Dependencies: 219
-- Data for Name: monthly_count; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.monthly_count (id, month, year, transaction_count) FROM stdin;
\.


--
-- TOC entry 3623 (class 0 OID 16399)
-- Dependencies: 215
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.transactions (id, transaction, transaction_date) FROM stdin;
\.


--
-- TOC entry 3638 (class 0 OID 0)
-- Dependencies: 216
-- Name: balance_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.balance_id_seq', 17, true);


--
-- TOC entry 3639 (class 0 OID 0)
-- Dependencies: 218
-- Name: monthly_count_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.monthly_count_id_seq', 12, true);


--
-- TOC entry 3640 (class 0 OID 0)
-- Dependencies: 214
-- Name: transactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.transactions_id_seq', 2, true);


--
-- TOC entry 3477 (class 2606 OID 16411)
-- Name: balance balance_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.balance
    ADD CONSTRAINT balance_pkey PRIMARY KEY (id);


--
-- TOC entry 3479 (class 2606 OID 16432)
-- Name: monthly_count monthly_count_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.monthly_count
    ADD CONSTRAINT monthly_count_pkey PRIMARY KEY (id);


--
-- TOC entry 3475 (class 2606 OID 16404)
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id);


-- Completed on 2023-06-06 20:27:04 CST

--
-- PostgreSQL database dump complete
--

