<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<tagfile doxygen_version="1.9.5" doxygen_gitid="0438643e8352d8a59d7f8846be554762bb5651b0*">
  <compound kind="class">
    <name>SQLamarr::AbsDataLoader</name>
    <filename>classSQLamarr_1_1AbsDataLoader.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <member kind="function">
      <type></type>
      <name>BaseSqlInterface</name>
      <anchorfile>classSQLamarr_1_1AbsDataLoader.html</anchorfile>
      <anchor>a0ba52a750eb8416ac92daf1cc1988e03</anchor>
      <arglist>(SQLite3DB &amp;db)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>int</type>
      <name>insert_event</name>
      <anchorfile>classSQLamarr_1_1AbsDataLoader.html</anchorfile>
      <anchor>ae1c0141ffdaf20e1b350d4b52fddfbe9</anchor>
      <arglist>(const std::string &amp;data_source, uint64_t run_number, uint64_t evt_number)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>int</type>
      <name>insert_collision</name>
      <anchorfile>classSQLamarr_1_1AbsDataLoader.html</anchorfile>
      <anchor>a46ac8dca278358d64ce19a2b479adc3b</anchor>
      <arglist>(int datasource_id, int collision, float t, float x, float y, float z)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>int</type>
      <name>insert_vertex</name>
      <anchorfile>classSQLamarr_1_1AbsDataLoader.html</anchorfile>
      <anchor>ab7c9acf4b02a1ef617b1933e5b3051f8</anchor>
      <arglist>(int genevent_id, int hepmc_id, int status, float t, float x, float y, float z, bool is_primary)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>int</type>
      <name>insert_particle</name>
      <anchorfile>classSQLamarr_1_1AbsDataLoader.html</anchorfile>
      <anchor>a84074e8024fa6208480903d141b84a80</anchor>
      <arglist>(int genevent_id, int hepmc_id, int production_vertex, int end_vertex, int pid, int status, float pe, float px, float py, float pz, float m)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::BaseSqlInterface</name>
    <filename>classSQLamarr_1_1BaseSqlInterface.html</filename>
    <member kind="function">
      <type></type>
      <name>BaseSqlInterface</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>a0ba52a750eb8416ac92daf1cc1988e03</anchor>
      <arglist>(SQLite3DB &amp;db)</arglist>
    </member>
    <member kind="function" virtualness="virtual">
      <type>virtual</type>
      <name>~BaseSqlInterface</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>a65ab16210bad711993ac17e41cbd021a</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>sqlite3_stmt *</type>
      <name>get_statement</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>a00f5c3677728266cc5b8cbb81a321495</anchor>
      <arglist>(const std::string &amp;name, const std::string &amp;query)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>begin_transaction</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>a4470177bd4b661eaa33d7161159825e3</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>end_transaction</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>aa7a8048e57b5760cc0560d4a34cc0c82</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>int</type>
      <name>last_insert_row</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>ab62ca26f443518966c427b8b99f0bffc</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>void</type>
      <name>using_sql_function</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>ad6f2a3074484638a89a06100cc4bf177</anchor>
      <arglist>(const std::string &amp;name, int argc, void(*xFunc)(sqlite3_context *, int, sqlite3_value **))</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>bool</type>
      <name>exec_stmt</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>abfa076f593bd2a9766972e4b02aec1a1</anchor>
      <arglist>(sqlite3_stmt *)</arglist>
    </member>
    <member kind="variable" protection="protected">
      <type>SQLite3DB &amp;</type>
      <name>m_database</name>
      <anchorfile>classSQLamarr_1_1BaseSqlInterface.html</anchorfile>
      <anchor>af20505c84b553f851785a70c25cd0719</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::c_TransformerPtr</name>
    <filename>classSQLamarr_1_1c__TransformerPtr.html</filename>
  </compound>
  <compound kind="class">
    <name>SQLamarr::CleanEventStore</name>
    <filename>classSQLamarr_1_1CleanEventStore.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <base>SQLamarr::Transformer</base>
    <member kind="function">
      <type>void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore.html</anchorfile>
      <anchor>aa7981d7bbc18dcf8417244834cb2c1b3</anchor>
      <arglist>() override</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>BaseSqlInterface</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore.html</anchorfile>
      <anchor>a0ba52a750eb8416ac92daf1cc1988e03</anchor>
      <arglist>(SQLite3DB &amp;db)</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore.html</anchorfile>
      <anchor>a681bb1401558a96c782637386a9fbafe</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore.html</anchorfile>
      <anchor>a1c65e28573a2b7dddde39af08edf8d48</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::CleanEventStore::CleanEventStore</name>
    <filename>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a45099c3650f7be93c6f7727c3a9a7001</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a45099c3650f7be93c6f7727c3a9a7001</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a45099c3650f7be93c6f7727c3a9a7001</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a45099c3650f7be93c6f7727c3a9a7001</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a45099c3650f7be93c6f7727c3a9a7001</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a08392f1adf5eb098784cc4cd2aec8ea7</anchor>
      <arglist>(self, db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>ad8e043edbbcf948157973d4f71e25e61</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a129a30ac818cd46bad748538139466ce</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1CleanEventStore_1_1CleanEventStore.html</anchorfile>
      <anchor>a45099c3650f7be93c6f7727c3a9a7001</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::GenerativePlugin</name>
    <filename>classSQLamarr_1_1GenerativePlugin.html</filename>
    <base>SQLamarr::Plugin::Plugin</base>
    <member kind="function">
      <type></type>
      <name>GenerativePlugin</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4aee8afdcbc9a78942e08eda3c4a00f2</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;library, const std::string &amp;function_name, const std::string &amp;select_query, const std::string &amp;output_table, const std::vector&lt; std::string &gt; outputs, unsigned int n_random, const std::vector&lt; std::string &gt; reference_keys={&quot;ref_id&quot;})</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin.html</anchorfile>
      <anchor>ad4f348e4fe0cca3a017cd463ab5a6191</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin.html</anchorfile>
      <anchor>a50934c1b49c68c64bf4bbdfba4d301fd</anchor>
      <arglist></arglist>
    </member>
    <member kind="typedef" protection="protected">
      <type>float *(*</type>
      <name>ganfunc</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin.html</anchorfile>
      <anchor>a775a2c8ed2b62ad457e301693b96b9cb</anchor>
      <arglist>)(float *, const float *, const float *)</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void</type>
      <name>eval_parametrization</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin.html</anchorfile>
      <anchor>aa3042c9a1a8fe6f54a9922cc4baa4019</anchor>
      <arglist>(float *output, const float *input)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::GenerativePlugin::GenerativePlugin</name>
    <filename>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4b9b429dff2738583fc934fa793974d7</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4b9b429dff2738583fc934fa793974d7</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4b9b429dff2738583fc934fa793974d7</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4b9b429dff2738583fc934fa793974d7</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4b9b429dff2738583fc934fa793974d7</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a65d5f72a93b255e9d21815f50353e667</anchor>
      <arglist>(self, db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>aef78d6fbbb94a75177871d062112fe06</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a22bff985653f7b4efa13f55e6b56e3c2</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1GenerativePlugin_1_1GenerativePlugin.html</anchorfile>
      <anchor>a4b9b429dff2738583fc934fa793974d7</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, int nRandom, List[str] references)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::HepMC2DataLoader</name>
    <filename>classSQLamarr_1_1HepMC2DataLoader.html</filename>
    <base>SQLamarr::AbsDataLoader</base>
    <member kind="function">
      <type>void</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a98451a3e3d0c2e12208c98da4a9f3e7b</anchor>
      <arglist>(const std::string &amp;file_path, size_t run_number, size_t evt_number)</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a659454b368a73764c29d03f224ea7ad7</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a7f7b775d008a7c418f4f5310a411b6c9</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::HepMC2DataLoader::HepMC2DataLoader</name>
    <filename>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a0504891ff5aaeb02952c16048872fe92</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a0504891ff5aaeb02952c16048872fe92</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a0504891ff5aaeb02952c16048872fe92</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a0504891ff5aaeb02952c16048872fe92</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a0504891ff5aaeb02952c16048872fe92</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>ab3afdade4eef97f0a467b5338c60e969</anchor>
      <arglist>(self, db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a761e370bc67636f8cf2ad3a2214cbac1</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a0504891ff5aaeb02952c16048872fe92</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>load</name>
      <anchorfile>classSQLamarr_1_1HepMC2DataLoader_1_1HepMC2DataLoader.html</anchorfile>
      <anchor>a06213d2ffb38ab6e45e7fc03f156755c</anchor>
      <arglist>(self, str filename, int runNumber, int evtNumber)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::MCParticleSelector</name>
    <filename>classSQLamarr_1_1MCParticleSelector.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <base>SQLamarr::Transformer</base>
    <member kind="function">
      <type></type>
      <name>MCParticleSelector</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>aa6b7183bb47428ae83ef38e55f9b4080</anchor>
      <arglist>(SQLite3DB &amp;db, const std::vector&lt; uint64_t &gt; retained_status_values={ LAMARR_LHCB_STABLE_IN_PRODGEN, LAMARR_LHCB_DECAYED_BY_DECAYGEN, LAMARR_LHCB_DECAYED_BY_DECAYGEN_AND_PRODUCED_BY_PRODGEN, LAMARR_LHCB_SIGNAL_IN_LAB_FRAME, LAMARR_LHCB_STABLE_IN_DECAYGEN }, const std::vector&lt; uint64_t &gt; retained_abspid_values={ 6, 22, 23, 24, 25, 32, 33, 34, 35, 36, 37, 102, 130, 310, 311, 321, 411, 421, 413, 423, 415, 425, 431, 435, 511, 521, 513, 523, 515, 525, 531, 535, 541, 545, 441, 10441, 100441, 443, 10443, 20443, 100443, 30443, 9000443, 9010443, 9020443, 445, 10445, 551, 10551, 100551, 110551, 200551, 210551, 553, 10553, 20553, 30553, 100553, 110553, 120553, 130553, 200553, 210553, 220553, 300553, 9000553, 9010553, 555, 10555, 20555, 100555, 110555, 120555, 200555, 557, 100557, 2212, 2212, 3122, 3222, 3212, 3224, 3214, 3114, 3322, 3312, 3324, 3314, 3334, 4122, 4222, 4212, 4112, 4224, 4214, 4114, 4232, 4132, 4322, 4312, 4324, 4314, 4332, 4334, 4412, 4422, 4414, 4424, 4432, 4434, 4444, 5122, 5112, 5212, 5222, 5114, 5214, 5224, 5132, 5232, 5312, 5322, 5314, 5324, 5332, 5334, 5142, 5242, 5412, 5422, 5414, 5424, 5342, 5432, 5442, 5444, 5512, 5522, 5514, 5524, 5532, 5534, 5542, 5544, 5554 })</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>a4ba1fa059f45b6f4a0791b475aab08bd</anchor>
      <arglist>() override</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>a4a78546f6e4b81b08291aa49aa45682e</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>a87c5331c391253340282f7bfef2df738</anchor>
      <arglist></arglist>
    </member>
    <member kind="function" protection="protected">
      <type>bool</type>
      <name>process_particle</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>a0f36bc588fe1e69d5b7796afe7370ce6</anchor>
      <arglist>(int genparticle_id, int prod_vtx)</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>bool</type>
      <name>keep</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>aede427557a8230d661425d7d225f6fbc</anchor>
      <arglist>(int status, int abspid) const</arglist>
    </member>
    <member kind="function" protection="protected">
      <type>uint64_t</type>
      <name>get_or_create_end_vertex</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector.html</anchorfile>
      <anchor>aa40060aed4b6c96881e07fbe4803fe71</anchor>
      <arglist>(int genparticle_id)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::MCParticleSelector::MCParticleSelector</name>
    <filename>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a6d8569044d2ca82f7ddce64fb3e4b2f9</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a6d8569044d2ca82f7ddce64fb3e4b2f9</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a6d8569044d2ca82f7ddce64fb3e4b2f9</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a6d8569044d2ca82f7ddce64fb3e4b2f9</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a6d8569044d2ca82f7ddce64fb3e4b2f9</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a1430de89d579295d542aca1fe76395af</anchor>
      <arglist>(self, db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a07a07a2b7f479a5d8a3ba9784b10fdf6</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a34028b8b9d3322da011c388ba8004ab2</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1MCParticleSelector_1_1MCParticleSelector.html</anchorfile>
      <anchor>a6d8569044d2ca82f7ddce64fb3e4b2f9</anchor>
      <arglist>(self, SQLite3DB db)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::Pipeline::Pipeline</name>
    <filename>classSQLamarr_1_1Pipeline_1_1Pipeline.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>a8214d76821f920ed5e7753860af8fc64</anchor>
      <arglist>(self, List[Any] algoritms)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Pipeline_1_1Pipeline.html</anchorfile>
      <anchor>af5c41b270e91d52385c43e4cccd4eaf5</anchor>
      <arglist>(self)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::Plugin</name>
    <filename>classSQLamarr_1_1Plugin.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <base>SQLamarr::Transformer</base>
    <member kind="function">
      <type></type>
      <name>Plugin</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>ad66dd0704648b74d472ec85d355a1797</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;library, const std::string &amp;function_name, const std::string &amp;select_query, const std::string &amp;output_table, const std::vector&lt; std::string &gt; outputs, const std::vector&lt; std::string &gt; reference_keys={&quot;ref_id&quot;})</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>a375d4e591a08cf39bc53ebe57fe96932</anchor>
      <arglist>() override</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>a5020d092db83085666f8b26483fa42bb</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>a78f5014c1b1c95464759a2d70603d145</anchor>
      <arglist></arglist>
    </member>
    <member kind="typedef" protection="protected">
      <type>float *(*</type>
      <name>mlfunc</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>af1684211c3736acdee3d733b5a908822</anchor>
      <arglist>)(float *, const float *)</arglist>
    </member>
    <member kind="function" protection="protected" virtualness="virtual">
      <type>virtual void</type>
      <name>eval_parametrization</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>a94f613b48f7c19ca4e2094d3bc026cb6</anchor>
      <arglist>(float *output, const float *input)</arglist>
    </member>
    <member kind="variable" protection="protected">
      <type>mlfunc</type>
      <name>m_func</name>
      <anchorfile>classSQLamarr_1_1Plugin.html</anchorfile>
      <anchor>ab5de29b68a2f3ab78c49b71decb10899</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::Plugin::Plugin</name>
    <filename>classSQLamarr_1_1Plugin_1_1Plugin.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a22e51facd69c9c5c0e839a8214e49236</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a22e51facd69c9c5c0e839a8214e49236</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a22e51facd69c9c5c0e839a8214e49236</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a22e51facd69c9c5c0e839a8214e49236</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a22e51facd69c9c5c0e839a8214e49236</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a59258bbc19b5c2fd08d2fde9b3ba2832</anchor>
      <arglist>(self, db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a85e61ede43e2d1c99bc33a0486f86f31</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a3907d744f2daae4ca3dab9b82da7feb9</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1Plugin_1_1Plugin.html</anchorfile>
      <anchor>a22e51facd69c9c5c0e839a8214e49236</anchor>
      <arglist>(self, SQLite3DB db, str library_path, str function_name, str query, str output_table, List[str] outputs, List[str] references)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::PVFinder</name>
    <filename>classSQLamarr_1_1PVFinder.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <base>SQLamarr::Transformer</base>
    <member kind="function">
      <type></type>
      <name>PVFinder</name>
      <anchorfile>classSQLamarr_1_1PVFinder.html</anchorfile>
      <anchor>a31a64cfe814e802cb5a18ca4b40d49b6</anchor>
      <arglist>(SQLite3DB &amp;db, int signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1PVFinder.html</anchorfile>
      <anchor>a59ce2b97e740f061197b0699b5eedc1d</anchor>
      <arglist>() override</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1PVFinder.html</anchorfile>
      <anchor>ac9da7099eaeafda719b160e65d256962</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1PVFinder.html</anchorfile>
      <anchor>aa2cf9f941e8f85f21960ac69e96d932c</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::PVFinder::PVFinder</name>
    <filename>classSQLamarr_1_1PVFinder_1_1PVFinder.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a0a42d94e0a760d8c52512653aa08adeb</anchor>
      <arglist>(self, SQLite3DB db, int signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a0a42d94e0a760d8c52512653aa08adeb</anchor>
      <arglist>(self, SQLite3DB db, int signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a0a42d94e0a760d8c52512653aa08adeb</anchor>
      <arglist>(self, SQLite3DB db, int signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a0a42d94e0a760d8c52512653aa08adeb</anchor>
      <arglist>(self, SQLite3DB db, int signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a0a42d94e0a760d8c52512653aa08adeb</anchor>
      <arglist>(self, SQLite3DB db, int signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>aac3a0c6e0b380d97eabe7bb1a0199228</anchor>
      <arglist>(self, db, signal_status_code=889)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>aea6cdb8f8aac7ebed25e081dbd8003a2</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a194e9a3d466aa531fc258df1269a46c1</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVFinder_1_1PVFinder.html</anchorfile>
      <anchor>a0a42d94e0a760d8c52512653aa08adeb</anchor>
      <arglist>(self, SQLite3DB db, int signal_status_code=889)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::PVReconstruction</name>
    <filename>classSQLamarr_1_1PVReconstruction.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <base>SQLamarr::Transformer</base>
    <member kind="function">
      <type></type>
      <name>PVReconstruction</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction.html</anchorfile>
      <anchor>a4f6272ea3f4fbd83cec5abe490dc56a6</anchor>
      <arglist>(SQLite3DB &amp;db, const SmearingParametrization &amp;parametrization)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction.html</anchorfile>
      <anchor>a2851d199c3e5aa32f0e9c3f97b8a3bf8</anchor>
      <arglist>() override</arglist>
    </member>
    <member kind="function" static="yes">
      <type>static SmearingParametrization</type>
      <name>load_parametrization</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction.html</anchorfile>
      <anchor>a0dd0331cf52d249e1512f5cce5880736</anchor>
      <arglist>(const std::string file_path, const std::string table_name, const std::string condition)</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction.html</anchorfile>
      <anchor>ae489fd2bc4078dabfdfc2fe9e0a84530</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction.html</anchorfile>
      <anchor>a2498f7f91112efc5277f52d1f81dd2f3</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::PVReconstruction::PVReconstruction</name>
    <filename>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a459d9c6de07c645457d9b1a067211fbe</anchor>
      <arglist>(self, SQLite3DB db, str file_name, str table_name, str condition)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a459d9c6de07c645457d9b1a067211fbe</anchor>
      <arglist>(self, SQLite3DB db, str file_name, str table_name, str condition)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a459d9c6de07c645457d9b1a067211fbe</anchor>
      <arglist>(self, SQLite3DB db, str file_name, str table_name, str condition)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a459d9c6de07c645457d9b1a067211fbe</anchor>
      <arglist>(self, SQLite3DB db, str file_name, str table_name, str condition)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a459d9c6de07c645457d9b1a067211fbe</anchor>
      <arglist>(self, SQLite3DB db, str file_name, str table_name, str condition)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>af23dfd546ad6782e32ad96b3ef23e5b2</anchor>
      <arglist>(self, db, str file_name, str table_name, str condition)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a4fa03fab55576f783c27773143569dda</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a7b4cbebc6c346abe9af0e7d439f68715</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PVReconstruction_1_1PVReconstruction.html</anchorfile>
      <anchor>a459d9c6de07c645457d9b1a067211fbe</anchor>
      <arglist>(self, SQLite3DB db, str file_name, str table_name, str condition)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::PyTransformer::PyTransformer</name>
    <filename>classSQLamarr_1_1PyTransformer_1_1PyTransformer.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1PyTransformer_1_1PyTransformer.html</anchorfile>
      <anchor>a17d94520b96c2eefcdacafe3cdc3a83e</anchor>
      <arglist>(self, db)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__call__</name>
      <anchorfile>classSQLamarr_1_1PyTransformer_1_1PyTransformer.html</anchorfile>
      <anchor>a7af34164d92b8fd1188e885d1a28745d</anchor>
      <arglist>(self, f)</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>SQLamarr::PVReconstruction::SmearingParametrization</name>
    <filename>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization.html</filename>
    <member kind="function">
      <type>SmearingParametrization_1D &amp;</type>
      <name>x</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization.html</anchorfile>
      <anchor>a9fa59d20868c4aa7a26a694ba72c11ae</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>SmearingParametrization_1D &amp;</type>
      <name>y</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization.html</anchorfile>
      <anchor>a96c609f06d05430bd1d70a0818dfe6b9</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>SmearingParametrization_1D &amp;</type>
      <name>z</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization.html</anchorfile>
      <anchor>aef04fe6f6c5e13d4e30ea4b8033e9665</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="variable">
      <type>std::array&lt; SmearingParametrization_1D, 3 &gt;</type>
      <name>data</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization.html</anchorfile>
      <anchor>a0ad94ac9a85a2ca0684f6fddd8c6726f</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>SQLamarr::PVReconstruction::SmearingParametrization_1D</name>
    <filename>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</filename>
    <member kind="variable">
      <type>float</type>
      <name>mu</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</anchorfile>
      <anchor>a9cf77a30a1bcfb5bd4bfca06fd488ea6</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>float</type>
      <name>f1</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</anchorfile>
      <anchor>a50f248e684cf6e84ea181059dda96e3f</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>float</type>
      <name>f2</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</anchorfile>
      <anchor>a992f02096bad8e433f0ea823f58b9887</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>float</type>
      <name>sigma1</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</anchorfile>
      <anchor>ac20482f9dd0c6494247011d1523aedbd</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>float</type>
      <name>sigma2</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</anchorfile>
      <anchor>a2e70f8724251816a0ef78ae55ba42fe1</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>float</type>
      <name>sigma3</name>
      <anchorfile>structSQLamarr_1_1PVReconstruction_1_1SmearingParametrization__1D.html</anchorfile>
      <anchor>a679d8fc1cf960f1946778f042e585764</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::db_functions::SQLite3DB</name>
    <filename>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>ac36a12d7bdfbff40c32721bf18527845</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>get</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a22b40112889bec5addbbc653a1208faa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a5ab717ea9105220b923b7215180f6d9a</anchor>
      <arglist>(self, str path=&quot;file::memory:?cache=shared&quot;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>seed</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a43bd44f0656433a178faabf9aca608e3</anchor>
      <arglist>(self, int seed)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>connect</name>
      <anchorfile>classSQLamarr_1_1db__functions_1_1SQLite3DB.html</anchorfile>
      <anchor>a97ce1889efefe08c441f60b614d762aa</anchor>
      <arglist>(self)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::Pipeline::SQLiteError</name>
    <filename>classSQLamarr_1_1Pipeline_1_1SQLiteError.html</filename>
  </compound>
  <compound kind="class">
    <name>SQLamarr::SQLiteError</name>
    <filename>classSQLamarr_1_1SQLiteError.html</filename>
  </compound>
  <compound kind="class">
    <name>SQLamarr::T_GlobalPRNG</name>
    <filename>classSQLamarr_1_1T__GlobalPRNG.html</filename>
    <templarg>class PRNG</templarg>
    <member kind="function">
      <type></type>
      <name>T_GlobalPRNG</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>af4e7b75bcdac2b1fdb9db03dfbc17931</anchor>
      <arglist>(T_GlobalPRNG const &amp;)=delete</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>operator=</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>add8a210d5d3400514eb33b4761ead071</anchor>
      <arglist>(T_GlobalPRNG const &amp;)=delete</arglist>
    </member>
    <member kind="function" static="yes">
      <type>static T_GlobalPRNG &amp;</type>
      <name>handle</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>a5483645576f83dd0c29e2c897ea58014</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function" static="yes">
      <type>static PRNG *</type>
      <name>get_or_create</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>a524dae7a65f7edc38a8f087bdf727055</anchor>
      <arglist>(const sqlite3_context *db, uint64_t seed=no_seed)</arglist>
    </member>
    <member kind="function" static="yes">
      <type>static PRNG *</type>
      <name>get_or_create</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>a0d7d9aeb0cfa4c5e654d86587af162e4</anchor>
      <arglist>(const sqlite3 *db, uint64_t seed=no_seed)</arglist>
    </member>
    <member kind="function" static="yes">
      <type>static bool</type>
      <name>release</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>a7720a02c1be64b0c21268d64b5d9ca21</anchor>
      <arglist>(const sqlite3 *db)</arglist>
    </member>
    <member kind="variable" static="yes">
      <type>static constexpr uint64_t</type>
      <name>no_seed</name>
      <anchorfile>classSQLamarr_1_1T__GlobalPRNG.html</anchorfile>
      <anchor>aa524d65cfc67191ccc9c36452eb4b168</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::TemporaryTable</name>
    <filename>classSQLamarr_1_1TemporaryTable.html</filename>
    <base>SQLamarr::BaseSqlInterface</base>
    <base>SQLamarr::Transformer</base>
    <member kind="function">
      <type></type>
      <name>TemporaryTable</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable.html</anchorfile>
      <anchor>ac0e25a76a8a1b482f5b70252ec31ab4c</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;output_table, const std::vector&lt; std::string &gt; &amp;columns, const std::vector&lt; std::string &gt; &amp;select_statements, bool make_persistent=false)</arglist>
    </member>
    <member kind="function">
      <type></type>
      <name>TemporaryTable</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable.html</anchorfile>
      <anchor>a08312c9ca488f209829e6f02b5ccc645</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;output_table, const std::vector&lt; std::string &gt; &amp;columns, const std::string &amp;select_statement, bool make_persistent=false)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable.html</anchorfile>
      <anchor>a7003442f96a2cb61a6dc2e8379e9ade3</anchor>
      <arglist>() override</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable.html</anchorfile>
      <anchor>aaa15b2a461668b336427da59d07da931</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable.html</anchorfile>
      <anchor>a7c0a6c7d929b83d8a150aea85945be83</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::TemporaryTable::TemporaryTable</name>
    <filename>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</filename>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>ac10cd1de9e4e1dd6a67f487dc129aa1c</anchor>
      <arglist>(self, SQLite3DB db, str output_table, str outputs, str query, bool make_persistent=False)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>ac10cd1de9e4e1dd6a67f487dc129aa1c</anchor>
      <arglist>(self, SQLite3DB db, str output_table, str outputs, str query, bool make_persistent=False)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>ac10cd1de9e4e1dd6a67f487dc129aa1c</anchor>
      <arglist>(self, SQLite3DB db, str output_table, str outputs, str query, bool make_persistent=False)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>ac10cd1de9e4e1dd6a67f487dc129aa1c</anchor>
      <arglist>(self, SQLite3DB db, str output_table, str outputs, str query, bool make_persistent=False)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>ac10cd1de9e4e1dd6a67f487dc129aa1c</anchor>
      <arglist>(self, SQLite3DB db, str output_table, str outputs, str query, bool make_persistent=False)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>ad690cc42cc26c3d1a9c7a3ed19d2c422</anchor>
      <arglist>(self, db, str output_table, str outputs, str query, bool make_persistent)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__del__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>a83aa4db5afe5c1dad97622368fed2236</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>raw_pointer</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>a6c4b5f3053824d21290a345eb1f5ea56</anchor>
      <arglist>(self)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>__init__</name>
      <anchorfile>classSQLamarr_1_1TemporaryTable_1_1TemporaryTable.html</anchorfile>
      <anchor>a3ccfadc0f7fc89b2de8211c36cd2b846</anchor>
      <arglist>(self, SQLite3DB db, str output_table, List[str] outputs, Union[str, List[str]] query, bool make_persistent=False)</arglist>
    </member>
  </compound>
  <compound kind="class">
    <name>SQLamarr::Transformer</name>
    <filename>classSQLamarr_1_1Transformer.html</filename>
    <member kind="function" virtualness="pure">
      <type>virtual void</type>
      <name>execute</name>
      <anchorfile>classSQLamarr_1_1Transformer.html</anchorfile>
      <anchor>a5b4286cbd900d114b2fd55f4ba7a7b94</anchor>
      <arglist>()=0</arglist>
    </member>
  </compound>
  <compound kind="struct">
    <name>TransformerPtr</name>
    <filename>structTransformerPtr.html</filename>
    <member kind="variable">
      <type>TransformerType</type>
      <name>dtype</name>
      <anchorfile>structTransformerPtr.html</anchorfile>
      <anchor>a7a78e709348ed9ac8584487fc8aef918</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>void *</type>
      <name>p</name>
      <anchorfile>structTransformerPtr.html</anchorfile>
      <anchor>a0d67766c5b59a3131d777361a472f189</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>__version__</name>
    <filename>namespace____version____.html</filename>
    <member kind="variable">
      <type></type>
      <name>version</name>
      <anchorfile>namespace____version____.html</anchorfile>
      <anchor>aba7f34c5325d79be8a4525f919a8ef0c</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>pythontest</name>
    <filename>namespacepythontest.html</filename>
    <member kind="function">
      <type>def</type>
      <name>my_del</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>ae4603b4fd93f7eb6400919283888d767</anchor>
      <arglist>(c)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>get_version</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>af818397ab0ac953050d70f6bfa607411</anchor>
      <arglist>(c)</arglist>
    </member>
    <member kind="variable">
      <type>string</type>
      <name>filename</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a92f165722853a37ff4edca0c205d3ad1</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>db</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a32c8effaa5d2a4ccdf99961ca87ee894</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>loader</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a507db4c278501e5f804146a4dce98901</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>pv_finder</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a009317941ffef29f0733546fda18d0a0</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>mcps</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>aad324824985450167fca2d38abbec550</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>pvreco</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a64b748579f152d61cc975db6e1f85d54</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>acceptance_model</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a1fe62d354bcec30ca39edee522909aec</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>clean_all</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>ad91579673d7180c00e69ad20e46872ee</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>pipeline</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a50e03bc34ac18c9bae15d6bb73924379</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>df</name>
      <anchorfile>namespacepythontest.html</anchorfile>
      <anchor>a80a50b72eb581aa34b1657023f193d6a</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>setup</name>
    <filename>namespacesetup.html</filename>
    <member kind="variable">
      <type></type>
      <name>ext</name>
      <anchorfile>namespacesetup.html</anchorfile>
      <anchor>a8345a57adf0c9566a76dd0fa6dbba6df</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>ext_modules</name>
      <anchorfile>namespacesetup.html</anchorfile>
      <anchor>a1bf56ea61d1e9865f316116dca2fbfea</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr</name>
    <filename>namespaceSQLamarr.html</filename>
    <namespace>SQLamarr::_find_CDLL</namespace>
    <namespace>SQLamarr::BlockLib</namespace>
    <namespace>SQLamarr::CleanEventStore</namespace>
    <namespace>SQLamarr::db_functions</namespace>
    <namespace>SQLamarr::GenerativePlugin</namespace>
    <namespace>SQLamarr::HepMC2DataLoader</namespace>
    <namespace>SQLamarr::MCParticleSelector</namespace>
    <namespace>SQLamarr::Pipeline</namespace>
    <namespace>SQLamarr::Plugin</namespace>
    <namespace>SQLamarr::PVFinder</namespace>
    <namespace>SQLamarr::PVReconstruction</namespace>
    <namespace>SQLamarr::PyTransformer</namespace>
    <namespace>SQLamarr::TemporaryTable</namespace>
    <class kind="class">SQLamarr::AbsDataLoader</class>
    <class kind="class">SQLamarr::BaseSqlInterface</class>
    <class kind="class">SQLamarr::c_TransformerPtr</class>
    <class kind="class">SQLamarr::CleanEventStore</class>
    <class kind="class">SQLamarr::GenerativePlugin</class>
    <class kind="class">SQLamarr::HepMC2DataLoader</class>
    <class kind="class">SQLamarr::MCParticleSelector</class>
    <class kind="class">SQLamarr::Plugin</class>
    <class kind="class">SQLamarr::PVFinder</class>
    <class kind="class">SQLamarr::PVReconstruction</class>
    <class kind="class">SQLamarr::SQLiteError</class>
    <class kind="class">SQLamarr::T_GlobalPRNG</class>
    <class kind="class">SQLamarr::TemporaryTable</class>
    <class kind="class">SQLamarr::Transformer</class>
    <member kind="typedef">
      <type>std::unique_ptr&lt; sqlite3, void(*)(sqlite3 *)&gt;</type>
      <name>SQLite3DB</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>abc45094ddb8dd77eacd2c9f1505576b1</anchor>
      <arglist></arglist>
    </member>
    <member kind="typedef">
      <type>T_GlobalPRNG&lt; std::ranlux48 &gt;</type>
      <name>GlobalPRNG</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a4cf753307ca47068d87968de04b06158</anchor>
      <arglist></arglist>
    </member>
    <member kind="typedef">
      <type>T_GlobalPRNG&lt; std::mt19937 &gt;</type>
      <name>GlobalPRNG_MT</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a28bb3bbdcaf1c46d26b16f84b342aca2</anchor>
      <arglist></arglist>
    </member>
    <member kind="function">
      <type>SQLite3DB</type>
      <name>make_database</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a5242d26306386ad24ec98444c40dad55</anchor>
      <arglist>(std::string filename, int flags=SQLITE_OPEN_READWRITE|SQLITE_OPEN_CREATE|SQLITE_OPEN_URI, std::string init=std::string())</arglist>
    </member>
    <member kind="function">
      <type>sqlite3_stmt *</type>
      <name>prepare_statement</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a2d68266a80782afdc641cc8e2c07f76e</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;query)</arglist>
    </member>
    <member kind="function">
      <type>std::string</type>
      <name>dump_table</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>acc6e3e646501428732d4c082208a07e4</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;query)</arglist>
    </member>
    <member kind="function">
      <type>float</type>
      <name>read_as_float</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a56f3cbb22e60a3bf6f07662d03d97c5b</anchor>
      <arglist>(sqlite3_stmt *, int)</arglist>
    </member>
    <member kind="function">
      <type>void</type>
      <name>validate_token</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a3f5d610c7b0d6a90a1d001b6a31e19d1</anchor>
      <arglist>(const std::string &amp;token)</arglist>
    </member>
    <member kind="function">
      <type>std::string</type>
      <name>_string_field</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a9cf1332c90a169e73c2d11c05b127918</anchor>
      <arglist>(T *s, int length, int column_type)</arglist>
    </member>
    <member kind="function">
      <type>int</type>
      <name>_get_field_length</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a13bfba195a1ffb682574769a2ade934d</anchor>
      <arglist>(int column_type)</arglist>
    </member>
    <member kind="function">
      <type>PVReconstruction::SmearingParametrization_1D</type>
      <name>_get_param_line</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a523af3c2fec121a7c37f963d780f99d2</anchor>
      <arglist>(sqlite3_stmt *stmt, std::string condition, std::string coord)</arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>clib</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a2c606c472b9726abbe186a2189a59b67</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>acae059dbdd9d6ebb750b2d727d2528be</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>version</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>af58d1a5bf5511449fd1c067be0080ad7</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>cwd</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a99471567927880d52f3834560aa713fe</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>tuple</type>
      <name>resolution_attempts</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>ab9ca8aa286fa018a1db2411c786b9ad9</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>namespaceSQLamarr.html</anchorfile>
      <anchor>a98e3b79e25f18d0ea1a653141883b263</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::_find_CDLL</name>
    <filename>namespaceSQLamarr_1_1__find__CDLL.html</filename>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::BlockLib</name>
    <filename>namespaceSQLamarr_1_1BlockLib.html</filename>
    <namespace>SQLamarr::BlockLib::LbParticleId</namespace>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::BlockLib::LbParticleId</name>
    <filename>namespaceSQLamarr_1_1BlockLib_1_1LbParticleId.html</filename>
    <member kind="function">
      <type>GenerativePlugin</type>
      <name>make</name>
      <anchorfile>namespaceSQLamarr_1_1BlockLib_1_1LbParticleId.html</anchorfile>
      <anchor>a8b42b844ba32082a9538bb02cf366554</anchor>
      <arglist>(SQLite3DB &amp;db, const std::string &amp;library, const std::string &amp;function_name, const std::string &amp;output_table, const std::string &amp;particle_table, const std::string &amp;track_table, const int abspid)</arglist>
    </member>
    <member kind="function">
      <type>std::vector&lt; std::string &gt;</type>
      <name>get_column_names</name>
      <anchorfile>namespaceSQLamarr_1_1BlockLib_1_1LbParticleId.html</anchorfile>
      <anchor>aa9b76e060d9c05339075b45fe57b8be6</anchor>
      <arglist>(bool include_indices=true, bool include_outputs=true)</arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::CleanEventStore</name>
    <filename>namespaceSQLamarr_1_1CleanEventStore.html</filename>
    <class kind="class">SQLamarr::CleanEventStore::CleanEventStore</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::db_functions</name>
    <filename>namespaceSQLamarr_1_1db__functions.html</filename>
    <class kind="class">SQLamarr::db_functions::SQLite3DB</class>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>namespaceSQLamarr_1_1db__functions.html</anchorfile>
      <anchor>aa0c453e657fedb84bf14527ccbdd33c1</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>namespaceSQLamarr_1_1db__functions.html</anchorfile>
      <anchor>a761cef94d105f82ee0a7a2d08b2fea10</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::GenerativePlugin</name>
    <filename>namespaceSQLamarr_1_1GenerativePlugin.html</filename>
    <class kind="class">SQLamarr::GenerativePlugin::GenerativePlugin</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::HepMC2DataLoader</name>
    <filename>namespaceSQLamarr_1_1HepMC2DataLoader.html</filename>
    <class kind="class">SQLamarr::HepMC2DataLoader::HepMC2DataLoader</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::MCParticleSelector</name>
    <filename>namespaceSQLamarr_1_1MCParticleSelector.html</filename>
    <class kind="class">SQLamarr::MCParticleSelector::MCParticleSelector</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::Pipeline</name>
    <filename>namespaceSQLamarr_1_1Pipeline.html</filename>
    <class kind="class">SQLamarr::Pipeline::Pipeline</class>
    <class kind="class">SQLamarr::Pipeline::SQLiteError</class>
    <member kind="variable">
      <type></type>
      <name>argtypes</name>
      <anchorfile>namespaceSQLamarr_1_1Pipeline.html</anchorfile>
      <anchor>aaf215672ea18eef789b76c19ef22d2c7</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type></type>
      <name>restype</name>
      <anchorfile>namespaceSQLamarr_1_1Pipeline.html</anchorfile>
      <anchor>a99b2cf367ccd9a4182446781b70e7f57</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>int</type>
      <name>SQL_ERRORSHIFT</name>
      <anchorfile>namespaceSQLamarr_1_1Pipeline.html</anchorfile>
      <anchor>a7c9b0db3fbfed2bc53e3a9730b52503b</anchor>
      <arglist></arglist>
    </member>
    <member kind="variable">
      <type>int</type>
      <name>LOGIC_ERRORSHIFT</name>
      <anchorfile>namespaceSQLamarr_1_1Pipeline.html</anchorfile>
      <anchor>a51ba1ce59d53c68cfd929cbc08262231</anchor>
      <arglist></arglist>
    </member>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::Plugin</name>
    <filename>namespaceSQLamarr_1_1Plugin.html</filename>
    <class kind="class">SQLamarr::Plugin::Plugin</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::PVFinder</name>
    <filename>namespaceSQLamarr_1_1PVFinder.html</filename>
    <class kind="class">SQLamarr::PVFinder::PVFinder</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::PVReconstruction</name>
    <filename>namespaceSQLamarr_1_1PVReconstruction.html</filename>
    <class kind="class">SQLamarr::PVReconstruction::PVReconstruction</class>
    <class kind="struct">SQLamarr::PVReconstruction::SmearingParametrization</class>
    <class kind="struct">SQLamarr::PVReconstruction::SmearingParametrization_1D</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::PyTransformer</name>
    <filename>namespaceSQLamarr_1_1PyTransformer.html</filename>
    <class kind="class">SQLamarr::PyTransformer::PyTransformer</class>
  </compound>
  <compound kind="namespace">
    <name>SQLamarr::TemporaryTable</name>
    <filename>namespaceSQLamarr_1_1TemporaryTable.html</filename>
    <class kind="class">SQLamarr::TemporaryTable::TemporaryTable</class>
  </compound>
  <compound kind="namespace">
    <name>test_no_printout</name>
    <filename>namespacetest__no__printout.html</filename>
    <member kind="function">
      <type>def</type>
      <name>count_print_out</name>
      <anchorfile>namespacetest__no__printout.html</anchorfile>
      <anchor>a4450a237484634706ed00634f08bc141</anchor>
      <arglist>(str filename, str fmt=&apos;C++&apos;)</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>test_src</name>
      <anchorfile>namespacetest__no__printout.html</anchorfile>
      <anchor>a76a85623c937a96189a72cade9d637a4</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>test_include</name>
      <anchorfile>namespacetest__no__printout.html</anchorfile>
      <anchor>aad3d0e588f98171f27215a3e8530f7e3</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>test_python</name>
      <anchorfile>namespacetest__no__printout.html</anchorfile>
      <anchor>af9e67a8ed95daeb786c72cb4fffe0bde</anchor>
      <arglist>()</arglist>
    </member>
    <member kind="function">
      <type>def</type>
      <name>test_setup</name>
      <anchorfile>namespacetest__no__printout.html</anchorfile>
      <anchor>a8c39843b5eca16b827cfb1a4ff8b377c</anchor>
      <arglist>()</arglist>
    </member>
  </compound>
  <compound kind="page">
    <name>md_docs_md_Creating_the_wheel</name>
    <title>Distributing as a binary wheel</title>
    <filename>md_docs_md_Creating_the_wheel.html</filename>
  </compound>
  <compound kind="page">
    <name>md_docs_md_EXAMPLES</name>
    <title>Examples</title>
    <filename>md_docs_md_EXAMPLES.html</filename>
  </compound>
  <compound kind="page">
    <name>md_docs_md_SQLite3_extensions</name>
    <title>SQLamarr extensions to SQLite</title>
    <filename>md_docs_md_SQLite3_extensions.html</filename>
  </compound>
  <compound kind="page">
    <name>md_docs_md_Tests</name>
    <title>Test infrastructure</title>
    <filename>md_docs_md_Tests.html</filename>
  </compound>
  <compound kind="page">
    <name>index</name>
    <title>SQLamarr</title>
    <filename>index.html</filename>
    <docanchor file="index.html">md_README</docanchor>
  </compound>
</tagfile>
