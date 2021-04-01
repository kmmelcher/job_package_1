# -*- coding: utf-8 -*-

CONTRACT_BODY = """
<div class="points">
    <style>							
        ol-strong { font-weight: bold; }
        ol-normal { font-weight: normal;}
        ol .contract {
            list-style-type: none;
            counter-reset: item;
            margin: 0;
            padding: 0;
        }
        .contract ol > li {
            display: table;
            counter-increment: item;
            margin-bottom: 0.6em;
        }
        .contract ol > li:before {
            content: counters(item, ".") ". ";
            display: table-cell;
            padding-right: 0.6em;    
        }
        .contract li ol > li {
            margin: 0;
        }
        .contract li ol > li:before {
            content: counters(item, ".") " ";
        }
    </style>

    <ol class="contract ol-strong">
        <li>Vertragsgegenstand
            <ul class="list-inline ol-normal">
                <li>Die Regelungen dieses Rahmenvertrages entfalten nur Wirkungen, wenn eine Beauftragung besteht. In diesem Fall gelten primär dessen Regelungen sowie ergänzend die Regelungen dieses Rahmenvertrages. Entgegenstehende oder von diesen Regelungen abweichende Bedingungen des Auftragnehmers erkennt der Auftraggeber nicht an, es sei denn, der Auftraggeber hätte ausdrücklich schriftlich ihrer Geltung zugestimmt. Die Regelungen dieses Rahmenvertrages und des Einzelvertrages gelten auch dann, wenn der Auftraggeber in Kenntnis entgegenstehender oder von diesen Regelungen abweichende Bedingungen des Auftragnehmers die Leistungen vorbehaltlos ausführen lässt.</li>
            </ul>
        </li>

        <li>Projektausführung
            <ol class="ol-normal">
                <li>Der Auftragnehmer führt das Projekt in eigener Verantwortung nach den Grundsätzen ordnungsgemäßer Berufsausübung sachgemäß und sorgfältig aus.</li>
                <li>Der Auftragnehmer ist dabei berechtigt und sichert zu, ausschließlich eigene, fest angestellte Mitarbeiter zur Erfüllung seiner Verbindlichkeiten aus diesem Rahmenvertrag und den jeweiligen Projektverträgen einzusetzen. Der Einsatz von Subauftragnehmern ist dagegen nur nach vorheriger schriftlicher Zustimmung durch den Auftraggeber gestattet. Der Auftragnehmer setzt zur Ausführung des Projektes nur Mitarbeiter mit hierzu ausreichender Qualifikation ein. Die Qualifikation der Mitarbeiter ist auf Verlangen des Auftraggebers nachzuweisen. Mitarbeiter des Auftragnehmers sind dessen Erfüllungsgehilfen.</li>
                <li>Der Auftragnehmer verpflichtet sich, beim Einsatz eines Mitarbeiters, der nicht über die Staatsbürgerschaft eines EU-Staates verfügt, dem Auftraggeber vor dessen Einsatz im Rahmen eines Einzelvertrages eine Kopie von dessen Arbeits- und Aufenthaltserlaubnis für das Land, in dem der Einsatz erfolgen soll, vorzulegen. Der Auftragnehmer stellt sicher, dass der Mitarbeiter rechtzeitig vor Ablauf der Erlaubnis deren Erneuerung/Verlängerung beantragt, und verpflichtet sich, dem Auftraggeber unaufgefordert eine Kopie vorzulegen.</li>
                <li>Die Organisation, der vom Auftragnehmer zu erbringenden Leistungen, obliegt dem Auftragnehmer, bei dem auch das Weisungsrecht über das eigene Personal liegt.</li>
                <li>Die betriebliche Organisation und sonstige betriebliche Umstände beim Auftraggeber oder dessen Kunden werden dem Auftragnehmer im zur Projektausführung erforderlichen Umfang bekannt gemacht und sind zu beachten.</li>
                <li>Erfordert das Projekt nach Auffassung des Projektleiters, dass Tätigkeiten des Auftragnehmers beim Auftraggeber oder dessen Kunden ausgeführt werden, sind Zeit und Ort mit dem Projektleiter des Auftraggebers oder des Kunden abzustimmen. Die für die Projektausführung eventuell erforderliche technische Infrastruktur stellt der Auftraggeber oder dessen Kunde in geeigneter Weise zur Verfügung, soweit im Einzelvertrag nichts Abweichendes vereinbart ist.</li>
                <li>Der Auftragnehmer hat seine im Projekt tatsächlich erbrachten Leistungen durch Vorlage eines schriftlichen Nachweises zu belegen (bspw. Time-Sheet).</li>
            </ol>
        </li>

        <li>Dokumentation / Einweisung
            <ol class="ol-normal">
                <li>Soweit im Einzelvertrag vereinbart dokumentiert der Auftragnehmer seine Projekttätigkeiten ausführlich, vollständig und verständlich und übergibt dem Auftraggeber oder dessen Kunden die Dokumentation (Benutzerhandbuch, Programmierhandbuch, Object- und Source-Code einschließlich sämtlicher Entwicklungsunterlagen und -kommentare).</li>
                <li>Die Dokumentation muss den allgemeinen Richtlinien und besonderen Vorgaben des Auftraggebers oder dessen Kunden entsprechen. Die allgemeinen Richtlinien und besonderen Vorgaben werden dem Auftragnehmer rechtzeitig bekanntgeben. Der Auftraggeber kann verlangen, dass der Auftragnehmer weitere dem Auftraggeber oder dessen Kunden geeignet erscheinende Unterlagen anfertigt.</li>
                <li>Auf Wunsch des Auftraggebers oder dessen Kunden wird der Auftragnehmer dessen Personal in die Anwendung der Software und Dokumentation einweisen.</li>
            </ol>
        </li>

        <!-- Generates unwanted page break -->

        <li>Vergütung
            <ol class="ol-normal">
                <li>Die Vergütung erfolgt nur für tatsächlich erbrachte Leistungen und gegen entsprechenden schriftlichen Nachweis.</li>
                <li>In der vereinbarten Vergütung sind die Kosten für den Teil der erforderlichen Betriebsmittel und Büroflächen, die vom Kunden des Auftraggebers zur Verfügung gestellt werden, berücksichtigt. Spesen, Kilometergeld, Fahrtzeit und sonstige Nebenleistungen sind mit der Vergütung abgegolten, sofern sich aus der schriftlichen Beauftragung nichts anderes ergibt.</li>
                <li>Der Auftragnehmer rechnet monatlich nachträglich seine erbrachten Leistungen ab. Der jeweiligen Rechnung ist, der vom betreffenden Projektleiter unterzeichnete Nachweis im Original beizufügen, mit dem die für die einzelnen Tätigkeiten aufgewandten Zeiten belegt werden. Sofern Reisekosten abgerechnet werden, sind die entsprechenden. Belege in Kopie und entweder durch das ausgefüllte und vom Projektleiter unterzeichnete Formblatt zur Reisekostenabrechnung im Original oder durch eine separate Rechnung nachzuweisen. Das Fehlen eines der Dokumente, ein Fehler in einem Dokument, nicht nachvollziehbare Angaben und/ oder das Fehlen notwendiger Angaben hemmen die Fälligkeit der Rechnung.</li>
                <li>Dem Auftragnehmer steht keine Vergütung für die Fehlzeiten seiner Mitarbeiter zu, die durch Krankheit, Urlaub oder sonstige vom Auftraggeber oder dessen Kunden nicht zu vertretende Umstände verursacht werden. Ebenso erfolgt keine Vergütung, solange der Auftragnehmer/seine Mitarbeiter seine/ihre Leistung wegen Streik oder Aussperrung beim Auftraggeber oder dessen Kunden wegen höherer Gewalt oder sonstiger vom Auftraggeber/dessen Kunde nicht zu vertretender Umstände nicht erbringen können.</li>
                <li>Als selbständig tätiger Unternehmer ist der Auftragnehmer insbesondere auch für alle steuerlichen und sozialversicherungsrechtlichen Angelegenheiten, die sich aus der Erfüllung dieses Rahmenvertrages und der Projektverträge ergeben, z.B. auch für die Entrichtung von Steuern, Abgaben und Sozialversicherungsbeiträgen, selbst verantwortlich. Der Auftragnehmer ist verpflichtet, aufgrund dieses Rahmenvertrages und des jeweiligen Einzelvertrages anfallende Vergütung ordnungsgemäß zu versteuern und gegebenenfalls anfallende Mehrwertsteuer ordnungsgemäß abzuführen.</li>
                <li>Sämtliche Rechnungen sind innerhalb von 30 Tagen nach Zugang der Rechnung und der dazugehörigen korrekten Dokumente abzüglich besonderer Überweisungsgebühren (z.B. für Überweisungen ins Ausland) zur Zahlung fällig. Das Zahlungsziel kann nach Wunsch des Auftragnehmers, auf 21 Tage mit 2% Skonto oder auf 14 Tage mit 3% Skonto reduziert werden. Dies ist auf den einzelnen Rechnung zu vermerken.</li>
            </ol>
        </li>

        <li>Urheberrechte und Nutzungsrechte
            <ol class="ol-normal">
                <li>Der Auftraggeber/dessen Kunde soll in umfassender Weise in die Lage versetzt werden, die gemäß Einzelvertrag ggf. erstellten oder bearbeiteten Software-Programme, Teile davon und allen mit seinen Projekttätigkeiten in Zusammenhang stehenden Ergebnisse wie z.B. Unterlagen und Dokumentation (im Folgenden insgesamt: „Tätigkeitsergebnisse") in unveränderter oder veränderter Form unter Ausschluss des Auftragnehmers in jeder Hinsicht - auch gewerblich - zu verwerten und zu vermarkten, sei es im eigenen Unternehmen des Auftraggeber/des Kunden des Auftraggeber, sei es durch entgeltliche oder unentgeltliche Weitergabe an Dritte. Eingeschlossen ist das nicht ausschließliche Recht, ohne zusätzliche Vergütung alle im Rahmen des Einzelvertrages gemachten Erfindungen frei zu verwerten.</li>
                <li>Der Auftragnehmer räumt dem Auftraggeber/dessen Kunden mit deren Entstehen unwiderruflich die zeitlich, räumlich und inhaltlich unbegrenzten ausschließlichen und übertragbaren Nutzungsrechte an den von ihm erstellten Tätigkeitsergebnissen ein.</li>
                <li>Die eingeräumten Nutzungsrechte beinhalten auch das Recht, die Tätigkeitsergebnisse auf sämtliche Arten zu nutzen, unter anderem in beliebiger Weise die Programme in eigenen und/oder fremden Betrieben laufen zu lassen, sie zu vervielfältigen, zu verbreiten, vorzuführen, über sie öffentlich zu berichten, zu übersetzen und über Fernleitungen oder drahtlos zu übertragen, sowie das Recht, die Tätigkeitsergebnisse ohne Zustimmung des Auftragnehmers nach eigenem Ermessen zu bearbeiten, zu ändern oder in sonstiger Weise umzugestalten und die hierdurch geschaffenen Ergebnisse in gleicher Weise wie die ursprünglichen Fassungen der Tätigkeitsergebnisse zu verwerten.</li>
                <li>Der Auftragnehmer verpflichtet sich, auf Wunsch des Auftraggebers oder dessen Kunden auf den Tätigkeitsergebnissen auf die vorgenannten Nutzungsrechte durch einen entsprechenden Vermerk hinzuweisen.</li>
                <li>Der Auftragnehmer stellt sicher, dass eventuelle Rechte gemäß § 12 UrhG (Zustimmung des Urhebers zur Veröffentlichung seines Werkes), § 13 Satz 2 UrhG (Urhebernennung) und § 25 UrhG (Zugang zu Werkstücken) nicht geltend gemacht werden.</li>
                <li>Soweit das Ergebnis von Leistungen des Auftragnehmers gesondert rechtlich schutzfähig ist, (z.B. als Patent, Gebrauchsmuster oder Urheberrecht), stehen derartige Rechte dem Auftraggeber/dessen Kunde zu. Soweit Rechte des Auftragnehmers gemäß § 8 UrhG entstehen (Miturheberschaft), verzichtet der Auftragnehmer zugunsten des Auftraggebers/dessen Kunden auf seinen Anteil an den Verwertungsrechten. Die Erträge aus der Nutzung der im Rahmen der Urheberschaft erbrachten Leistungen des Auftragnehmers stehen ausschließlich dem Auftraggeber/dessen Kunde zu. Soweit die Mitwirkung des Auftragnehmers erforderlich ist, um schutzfähige Leistungen gemäß Satz 1 rechtlich zu schützen, ist der Auftragnehmer verpflichtet, dem Auftraggeber/dessen Kunden im erforderlichen Umfang zu unterstützen.</li>
                <li>Nach Abschluss der vertraglich vereinbarten Leistungen kann der Auftraggeber/dessen Kunde vom Auftragnehmer jederzeit verlangen, dass dieser sämtliche Originale und Kopien der Werke herausgibt und die vollständige Erfüllung dieser Verpflichtung schriftlich versichert. Soweit die Kopien auf maschinenlesbaren Datenträgern des Auftragnehmers aufgezeichnet sind, tritt an die Stelle der Herausgabe das Löschen der Aufzeichnungen.</li>
                <li>Der Auftraggeber / dessen Kunde ist frei, ohne Zustimmung des Auftragnehmers hinsichtlich einzelner oder sämtlicher ihm eingeräumten Rechte einfache oder ausschließliche. Nutzungsrechte Dritten einzuräumen oder die erworbenen Rechte ganz oder teilweise auf Dritte zu übertragen.</li>
                <li>Die Zahlung der Vergütung gemäß der jeweiligen Beauftragung umfasst die Einräumung der vorstehend genannten Rechte; insoweit wird keine weitere Vergütung geschuldet.</li>
            </ol>
        </li>

        <li>Freiheit von Rechten Dritter
            <ol class="ol-normal">
                <li>Der Auftragnehmer gewährleistet und sichert daneben zu, dass die von ihm erstellten Tätigkeitsergebnisse frei von Schutzrechten und sonstigen Rechten Dritter sind, welche die Nutzung gemäß Ziffer 5 dieses Rahmenvertrages einschränken oder ausschließen. Der Auftragnehmer stellt insbesondere durch entsprechende Vereinbarungen mit seinen Mitarbeitern sicher, dass die Nutzung gemäß Ziffer 5 dieses Rahmenvertrages nicht durch eventuelle Urheber- oder sonstige Rechte beeinträchtigt wird. Auf Wunsch des Auftraggebers wird der Auftragnehmer dem Auftraggeber den Abschluss entsprechender Vereinbarungen mit den Mitarbeitern nachweisen.</li>
                <li>Der Auftragnehmer übernimmt die alleinige Haftung gegenüber denjenigen, die eine Verletzung von Schutzrechten geltend machen. Er wird den Auftraggeber sofort von sämtlichen derartigen Ansprüchen freistellen und sämtliche damit in Zusammenhang stehenden Nachteile und Schäden ohne jegliche Haftungsbegrenzung ersetzen.</li>
                <li>Wird die vertragsgemäße Nutzung durch Schutzrechte Dritter beeinträchtigt, hat der Auftragnehmer in einem für den Auftraggeber/dessen Kunden zumutbaren Umfang das Recht, nach seiner Wahl entweder die vertraglichen Leistungen so zu ändern, dass sie aus dem Schutzbereich herausfallen, gleichwohl aber den vertraglichen Bestimmungen entsprechen, oder die Befugnis zu erwirken, dass sie uneingeschränkt und ohne zusätzliche Kosten für den Auftraggeber und dessen Kunden vertragsgemäß genutzt werden können.</li>
                <li>Der Auftraggeber und dessen Kunde ist jeweils berechtigt, einem eventuellen Rechtsstreit des Auftragnehmers mit einem Dritten über dessen geltend gemachte Schutzrechte beizutreten. Die ihm und seinem Kunden entstehenden Kosten für die Durchführung des Rechtsstreits trägt hierbei jede Partei jeweils für sich.</li>
            </ol>
        </li>

        <li>Nutzung bereitgestellter Ressourcen
            <ol class="ol-normal">
                <li>Sofern aus Sicherheitsgründen vom Auftraggeber/Kunden technische Ressourcen bereitgestellt werden (Hardware, Software-Programme, Leitungskapazität und sonstige Infrastruktur), ist die Nutzung allein für Zwecke des Auftraggebers/dessen Kunde zulässig.</li>
                <li>Eine Vervielfältigung oder Verbreitung der vom Auftraggeber/dessen Kunde bereitgestellten Softwareprogramme oder Daten auf Rechner des Auftragnehmers ist nur nach vorheriger schriftlicher Zustimmung des Auftraggebers/dessen Kunde gestattet. Gleiches gilt für das Übertragen von Programmen seitens des Auftragnehmers auf einen Rechner des Auftraggebers/dessen Kunde. Der Auftraggeber/dessen Kunde ist berechtigt, sich mittels DV-technischer Kontrollen davon zu vergewissern, dass die dem Auftragnehmer durch den Auftraggeber/dessen Kunde bereitgestellten technischen und sonstigen Ressourcen nur zur Erfüllung der vertraglich geschuldeten Leistungen verwendet werden.</li>
                <li>Bei missbräuchlicher Nutzung durch vom Auftraggeber/dessen Kunden bereitgestellter Ressourcen haftet der Auftragnehmer für alle Schäden, die dem Auftraggeber/dessen Kunde dadurch entstehen, dass Dritte Schadensersatz für die unberechtigte Nutzung geltend machen, sowie für die sonstigen Kosten, die dem Auftraggeber/dessen Kunde durch die missbräuchliche Nutzung entstehen.</li>
            </ol>
        </li>

        <li>Geheimhaltung, Datenschutz, Umweltschutz
            <ol class="ol-normal">
                <li>Der Auftragnehmer verpflichtet sich, die gesetzlichen Bestimmungen über den Datenschutz einzuhalten und alle aus dem Bereich des Auftraggeber und dessen Kunden erlangten Informationen, insbesondere Geschäftsgeheimnisse, Unterlagen und Informationen über deren jeweilige Kunden, sowie alle im Zusammenhang mit einem Projekt erlangten Arbeitsergebnisse und Erkenntnisse geheim zu halten und nicht an andere Dritte als den betreffenden Kunden des Auftraggeber weiterzugeben, zu veröffentlichen oder sonst zu verwerten. Dies gilt insbesondere bezüglich aller Informationen, die sich aus der Nutzung von nicht dem Auftragnehmer zustehenden technischen und personellen Ressourcen ergeben, und bezüglich sicherheitsrelevanter und personenbezogener Daten, die dem Auftragnehmer zur Kenntnis kommen.</li>
                <li>Die dem Auftragnehmer überlassenen Unterlagen und Dokumente sind so aufzubewahren, dass sie nur innerhalb des jeweiligen Projektes den dem Auftraggeber benannten Mitarbeitern des Auftragnehmers zugänglich sind. Die Unterlagen und Dokumente sind nach Abschluss des Projektes an den Auftraggeber/dessen Kunden zurückzugeben. Zurückbehaltungsrechte an den Unterlagen und Dokumenten stehen dem Auftragnehmer - gleich aus welchem Rechtsgrund – nicht zu.</li>
                <li>Der Auftragnehmer wird alle Personen, die von ihm mit der Bearbeitung/Erfüllung eines Einzelvertrages betraut sind, auch für die Zeit nach Projektende/Ausscheiden aus den Diensten des Auftragnehmers entsprechend verpflichten. Der Auftragnehmer hat diese Verpflichtungen schriftlich vorzunehmen und sie der Auftraggeber auf Verlangen vorzulegen. Der Auftragnehmer wird auf Anfordern des Auftraggebers den betreffenden Personenkreis namentlich bekanntgeben. Der Auftragnehmer wird mit der gebotenen Sorgfalt darauf hinwirken, dass dieser Personenkreis die aus dem Bereich des Auftraggebers und dessen Kunden erlangten Informationen streng vertraulich behandelt, und einen Missbrauch verhindern. Der Auftraggeber ist unverzüglich zu informieren, wenn Anhaltspunkte dafür bestehen, dass über den genannten Personenkreis hinaus Dritte Kenntnisse von Daten gemäß Ziffer 8.a erhalten haben könnten.</li>
                <li>Der Auftragnehmer unterrichtet den Auftraggeber unverzüglich bei Verdacht auf Geheimhaltungs- und/oder Datenschutzverletzungen und bei Anlassprüfungen durch die Aufsichtsbehörde, wenn diese sich auf Daten des Auftraggebers und/oder dessen Kunden beziehen.</li>
                <li>Der Auftragnehmer verpflichtet sich ferner, strengstes Stillschweigen über den gesamten Inhalt dieses Rahmenvertrages und aller Projektverträge zu bewahren. Ausgenommen davon sind Rechtsbeistände des Auftragnehmers.</li>
                <li>Der Auftragnehmer verpflichtet sich, für jeden Fall der Zuwiderhandlung gegen vorstehende Verpflichtungen dieser Ziffer 8 - auch durch einen Mitarbeiter - jeweils eine Vertragsstrafe in Höhe von EUR 25.000, -- zu zahlen. Die Einrede des Fortsetzungszusammenhangs ist ausgeschlossen. Weitergehende Schadensersatzansprüche bleiben vorbehalten.</li>
                <li>Sämtliche vorstehende Verpflichtungen gemäß dieser Ziffer 8 bestehen auch nach Beendigung dieses Rahmenvertrages sowie aller Projektverträge fort.</li>
                <li>Der Auftragnehmer verpflichtet sich, in Erfüllung dieses Rahmenvertrages und aller Projektverträge nur solche Produkte zu liefern und/oder solche Techniken einzusetzen, die in Bezug auf Herstellung, Anwendung und Entsorgung den Bestimmungen des jeweils geltenden Umweltschutzrechts Rechnung tragen. Der Auftragnehmer stellt den Auftraggeber/dessen Kunden von sämtlichen Ansprüchen Dritter wegen der Verletzung von umweltschutzrechtlich relevanten Bestimmungen frei und verpflichtet sich, dem Auftraggeber/dessen Kunden sämtliche Schäden und etwaige Geldbußen zu er setzen, zu deren Zahlung sie wegen Verletzung der genannten Bestimmungen in Anspruch genommen werden.</li>
            </ol>
        </li>

        <li>Anwendbares Recht und Gerichtsstand
            <ol class="ol-normal">
                <li>Dieser Vertrag sowie die einzelnen Projektverträge unterliegen ausschließlich dem Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts.</li>
                <li>Gerichtsstand für alle Streitigkeiten aus oder in Verbindung mit diesem Vertrag und/oder einem Einzelvertrag ist der Sitz des Auftraggebers.</li>
            </ol>
        </li>

        <!-- Generates unwanted page break -->

        <li>Sonstiges
            <ol class="ol-normal">
                <li>Der Auftragnehmer sichert zu, über alle behördlichen Erlaubnisse zu verfügen und alle behördlichen Anmeldungen vorgenommen zu haben, die für die Erfüllung dieses Rahmenvertrages und der Projektverträge erforderlich sind, und rechtzeitig für deren Erneuerung/Verlängerung zu sorgen.</li>
                <li>Der Auftragnehmer ist berechtigt, jederzeit für Dritte tätig zu werden. Sofern es sich bei Dritten um Wettbewerber des Auftraggebers handelt, ist der Auftragnehmer verpflichtet, durch geeignete Maßnahmen sicherzustellen, dass seine Verpflichtungen unter diesem Rahmenvertrag sowie aller Projektverträge ordnungsgemäß erfüllt werden können, insbesondere die Verpflichtung zur Geheimhaltung gemäß diesem Rahmenvertrag.</li>
                <li>Sollten Dritte, seien es Mitarbeiter, sonstige Vertragspartner des Auftragnehmers, Behörden oder ähnliche Institutionen gegenüber dem Auftraggeber Ansprüche mit der Behauptung geltend machen, dass der Abschluss oder die Durchführung dieses Rahmenvertrages und/oder eines Einzelvertrages gegen die mit ihnen bestehenden vertraglichen Regelungen oder öffentlich-rechtliche Bestimmungen (insbesondere Gesetze, Rechtsvorschriften, Verwaltungsrichtlinien und so weiter) verstoßen, wird der Auftragnehmer sofort die notwendigen Maßnahmen ergreifen oder Vertragsänderungen vornehmen, um eine Verletzung solcher Ansprüche oder Bestimmungen zu vermeiden. Er wird darüber hinaus den Auftraggeber sofort von jeglichen Ansprüchen freistellen und etwaige Schäden oder Nachteile, die dem Auftraggeber aufgrund der Geltendmachung der Ansprüche entstehen, unbeschränkt ersetzen.</li>
                <li>Rechte und Pflichten aus diesem Vertrag sowie aus einem Einzelvertrag kann der Auftragnehmer nur nach vorheriger schriftlicher Zustimmung des Auftraggebers auf einen Dritten übertragen.</li>
                <li>Dieser Vertrag enthält neben den noch zu schließenden Beauftragungen sämtliche Vereinbarungen zwischen den Vertragspartnern und ersetzt eventuelle frühere Vereinbarungen zwischen ihnen. Mündliche Nebenabreden bestehen nicht.</li>
                <li>Ergänzungen, Änderungen oder Aufhebungen dieses Rahmenvertrages sowie eines Einzelvertrages oder die Kündigung eines Einzelvertrages bedürfen der Schriftform. Auch die Änderung dieses Schriftformerfordernisses bedarf der Schriftform.</li>
                <li>Sollten einzelne Bestimmungen dieses Vertrages oder eines Einzelvertrages ganz oder teilweise unwirksam oder nicht durchführbar sein, oder sollte sich in diesem Vertrag eine Lücke befinden, so wird hierdurch die Gültigkeit der übrigen Bestimmungen dieses Vertrages nicht berührt. Anstelle der unwirksamen oder undurchführbaren Bestimmungen gilt diejenige wirksame Bestimmung als vereinbart, die dem wirtschaftlichen Zweck der unwirksamen Bestimmung am nächsten kommt. Im Falle einer Lücke gilt diejenige Bestimmung als vereinbart, die dem entspricht, was nach dem Zweck dieses Vertrages vereinbart worden wäre, hätten die Vertragsparteien die Angelegenheit von vornherein bedacht.</li>
            </ol>
        </li>  
    </ol>

</div>
"""