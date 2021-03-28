# -*- coding: utf-8 -*-

CONTRACT_BODY = """
<div class="points">
    <style>							
        .ol-strong { font-weight: bold; }
        .ol-normal { font-weight: normal;}
        ol {
            list-style-type: none;
            counter-reset: item;
            margin: 0;
            padding: 0;
        }

        ol > li {
            display: table;
            counter-increment: item;
            margin-bottom: 0.6em;
        }

        ol > li:before {
            content: counters(item, ".") ". ";
            display: table-cell;
            padding-right: 0.6em;    
        }

        li ol > li {
            margin: 0;
        }

        li ol > li:before {
            content: counters(item, ".") " ";
        }
    </style>
    
    <ol class="ol-strong">

        <li>Lorem ipsum:
            <ol class="ol-normal">
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.Mauris posuere turpis vitae sem ullamcorper, at pellentesque justo interdum.Cras tempor erat ac posuere varius.</li>
                <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus at sapien scelerisque, scelerisque turpis ut, suscipit urna. Mauris ultricies vitae mauris ullamcorper pulvinar. Nulla facilisi.</li>
                <li>Curabitur consectetur ipsum id interdum imperdiet. Donec gravida, mauris luctus auctor bibendum, sem leo bibendum dolor, a sagittis libero enim nec tortor. Nam laoreet risus mi, laoreet hendrerit mi varius ac. Duis condimentum risus lacus, non bibendum diam vestibulum id.</li>
                <li>Aenean lobortis lorem vel tellus dignissim egestas. Nulla blandit facilisis ipsum a gravida. Cras scelerisque fringilla dolor quis tincidunt.</li>
                <li>Etiam viverra, odio sed sodales feugiat, urna neque varius urna, nec tristique tellus purus ut nibh. Maecenas sit amet augue et est finibus tristique. Cras egestas tortor vel libero interdum posuere.</li>
            </ol>
        </li>
        
        <li>Vivamus:
            <ul class="list-inline ol-normal">
                <li>Proin sed dolor efficitur, rhoncus quam vel, fermentum massa.</li>
                <li>Mauris quis eros iaculis, posuere massa vitae, pretium ante.</li>
                <li>Sed iaculis dolor vel libero sodales euismod.</li>
                <li>In accumsan ante id lectus aliquam gravida.</li>
                <li>Vestibulum tincidunt neque vitae lobortis placerat.</li>
            </ul>
        </li>
        
        <li>Cras eget ligula sit amet libero sodales
            <ol class="ol-normal">
                <li>Donec tincidunt orci eu nulla interdum maximus.</li>
                <li>Morbi malesuada turpis eu elit dapibus sagittis.</li>
            </ol>
        </li>
        
    </ol>
</div>
"""