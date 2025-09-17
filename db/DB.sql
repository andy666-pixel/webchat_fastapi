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
-- Name: message; Type: TABLE; Schema: public; Owner: andy
--

CREATE TABLE public.message (
    id integer NOT NULL,
    content text NOT NULL,
    sender_id integer NOT NULL,
    receiver_id integer NOT NULL,
    "timestamp" date NOT NULL
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
-- Name: message id; Type: DEFAULT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.message ALTER COLUMN id SET DEFAULT nextval('public.message_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: message message_pkey; Type: CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_pkey PRIMARY KEY (id);


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
-- Name: message message_receiver_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_receiver_id_fkey FOREIGN KEY (receiver_id) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- Name: message message_sender_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: andy
--

ALTER TABLE ONLY public.message
    ADD CONSTRAINT message_sender_id_fkey FOREIGN KEY (sender_id) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

