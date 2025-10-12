--
-- PostgreSQL database dump
--

-- Dumped from database version 15.13 (Debian 15.13-0+deb12u1)
-- Dumped by pg_dump version 15.13 (Debian 15.13-0+deb12u1)

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
-- Name: public; Type: SCHEMA; Schema: -; Owner: andy
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO andy;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: contacts; Type: TABLE; Schema: public; Owner: andy
--

CREATE TABLE public.contacts (
    id integer NOT NULL,
    user_id integer NOT NULL,
    contact_id integer NOT NULL
);


ALTER TABLE public.contacts OWNER TO andy;

--
-- Name: contacts_id_seq; Type: SEQUENCE; Schema: public; Owner: andy
--

CREATE SEQUENCE public.contacts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contacts_id_seq OWNER TO andy;

--
-- Name: contacts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: andy
--

ALTER SEQUENCE public.contacts_id_seq OWNED BY public.contacts.id;


--
-- Name: message; Type: TABLE; Schema: public; Owner: andy
--

CREATE TABLE public.message (
    id integer NOT NULL,
    content text NOT NULL,
    sender_name text NOT NULL,
    receiver_name text,
    "timestamp" timestamp without time zone
);


ALTER TABLE public.message OWNER TO andy;

--
-- Name: message_id_seq; Type: SEQUENCE; Schema: public; Owner: andy
--

CREATE SEQUENCE public.message_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.message_id_seq OWNER TO andy;

--
-- Name: message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: andy
--

ALTER SEQUENCE public.message_id_seq OWNED BY public.message.id;


--
-- Name: room; Type: TABLE; Schema: public; Owner: andy
--

CREATE TABLE public.room (
    id integer NOT NULL,
    room_name text NOT NULL,
    users text NOT NULL,
    sender_message_name text NOT NULL
);


ALTER TABLE public.room OWNER TO andy;

--
-- Name: room_id_seq; Type: SEQUENCE; Schema: public; Owner: andy
--

CREATE SEQUENCE public.room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.room_id_seq OWNER TO andy;

--
-- Name: room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: andy
--

ALTER SEQUENCE public.room_id_seq OWNED BY public.room.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: andy
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    name text NOT NULL,
    is_online boolean DEFAULT false NOT NULL,
    email text,
    hashed_password character varying NOT NULL,
    disabled boolean DEFAULT false NOT NULL
);


ALTER TABLE public."user" OWNER TO andy;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: andy
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO andy;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: andy
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: contacts id; Type: DEFAULT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.contacts ALTER COLUMN id SET DEFAULT nextval('public.contacts_id_seq'::regclass);


--
-- Name: message id; Type: DEFAULT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.message ALTER COLUMN id SET DEFAULT nextval('public.message_id_seq'::regclass);


--
-- Name: room id; Type: DEFAULT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.room ALTER COLUMN id SET DEFAULT nextval('public.room_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: contacts; Type: TABLE DATA; Schema: public; Owner: andy
--

COPY public.contacts (id, user_id, contact_id) FROM stdin;
\.


--
-- Data for Name: message; Type: TABLE DATA; Schema: public; Owner: andy
--

COPY public.message (id, content, sender_name, receiver_name, "timestamp") FROM stdin;
3	dasdsa	string	\N	2025-10-07 19:27:18.323853
4	dasdas	string	\N	2025-10-07 19:27:23.891066
5	asdasdasd	string	\N	2025-10-07 19:27:25.945079
6	holaaa	string	\N	2025-10-07 19:27:29.27112
\.


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: andy
--

COPY public.room (id, room_name, users, sender_message_name) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: andy
--

COPY public."user" (id, name, is_online, email, hashed_password, disabled) FROM stdin;
1	string	f	string@string.com	$2b$12$jWPIE6D.4Laivnxmdnu8OOOMRi0xyMqWHEsp6j/iTNK6cZcbqiTWO	f
13	hola	f	hola@gmail.com	$2b$12$aCBhKG2gOyEbTiCW/w.s0OyDOwXQ1GZlEJLpFEdhQQ0pTdLIEmzxO	t
\.


--
-- Name: contacts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: andy
--

SELECT pg_catalog.setval('public.contacts_id_seq', 1, false);


--
-- Name: message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: andy
--

SELECT pg_catalog.setval('public.message_id_seq', 6, true);


--
-- Name: room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: andy
--

SELECT pg_catalog.setval('public.room_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: andy
--

SELECT pg_catalog.setval('public.user_id_seq', 13, true);


--
-- Name: contacts contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (id);


--
-- Name: contacts contacts_user_id_contact_id_key; Type: CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_user_id_contact_id_key UNIQUE (user_id, contact_id);


--
-- Name: message message_pkey; Type: CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_pkey PRIMARY KEY (id);


--
-- Name: room room_pkey; Type: CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: idx_user_email; Type: INDEX; Schema: public; Owner: andy
--

CREATE UNIQUE INDEX idx_user_email ON public."user" USING btree (email);


--
-- Name: idx_user_name; Type: INDEX; Schema: public; Owner: andy
--

CREATE UNIQUE INDEX idx_user_name ON public."user" USING btree (name);


--
-- Name: contacts contacts_contact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- Name: contacts contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

